import os

from django.contrib import messages
from django.core.files.storage import default_storage
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.text import get_valid_filename

from .forms import FileUploadForm
from .models import UploadedFile


def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["file"]
            if file.name.endswith(".py"):
                user = request.user
                user_folder = f"uploads/user_{user.id}"
                # Используем ID пользователя для уникальности
                filename = get_valid_filename(file.name)
                file_path = os.path.join(user_folder, filename)

                # Проверка, есть ли уже такой файл у пользователя
                existing_files = UploadedFile.objects.filter(
                    user=user, file=file_path
                )
                if existing_files:
                    existing_file = existing_files.first()
                    default_storage.delete(existing_file.file.path)
                    existing_file.file = file  # Заменить файл на новый
                    existing_file.inspected = False
                    existing_file.save()
                else:
                    uploaded_file = UploadedFile(user=user, file=file_path)
                    uploaded_file.save()
                    default_storage.save(file_path, file)  # Сохранить файл

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