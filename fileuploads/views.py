import os

from django.contrib import messages
from django.core.files.storage import default_storage
from django.db import transaction
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.text import get_valid_filename

from .forms import FileUploadForm
from .models import InspectionLog, UploadedFile


def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["file"]
            if file.name.endswith(".py"):
                user = request.user
                user_folder = f"uploads/user_{user.id}"

                filename = get_valid_filename(file.name)
                file_path = os.path.join(user_folder, filename)

                existing_files = UploadedFile.objects.filter(
                    user=user, file=file_path
                )
                if existing_files:
                    with transaction.atomic():
                        existing_file = existing_files.first()
                        default_storage.delete(existing_file.file.path)
                        existing_file.file = file
                        existing_file.inspected = False
                        existing_file.save()
                        log = InspectionLog.objects.create(
                            uploaded_file=existing_file,
                            massage=f"update file {existing_file.file.name}",
                        )
                        log.save()
                else:
                    with transaction.atomic():
                        uploaded_file = UploadedFile(user=user, file=file_path)
                        default_storage.save(file_path, file)
                        uploaded_file.save()
                        log = InspectionLog.objects.create(
                            uploaded_file=uploaded_file,
                            massage=f"load file {uploaded_file.file.name}",
                        )
                        log.save()

                messages.success(request, "Файл успешно загружен.")
                return redirect("file_list")
            else:
                messages.error(request, "Недопустимое расширение файла.")
    else:
        form = FileUploadForm()
    return render(request, "fileuploads/upload_file.html", {"form": form})


def file_list(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, "fileuploads/file_list.html", {"files": files})


def delete_file(request, file_id):
    try:
        uploaded_file = UploadedFile.objects.get(id=file_id, user=request.user)
        file_path = uploaded_file.file.path

        default_storage.delete(file_path)
        uploaded_file.delete()

        messages.success(request, "Файл успешно удален.")
    except UploadedFile.DoesNotExist:
        raise Http404("Указанный файл не существует.")

    return redirect("file_list")
