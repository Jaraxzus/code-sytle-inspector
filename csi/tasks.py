from collections import defaultdict

from celery import shared_task
from django.contrib.auth.models import User
from django.db import transaction
from fileuploads.models import InspectionLog, UploadedFile
from notifications.tasks import mail_user

from csi.utils import check_style


@shared_task
def inspection():
    files_objects = UploadedFile.objects.filter(inspected=False).order_by(
        "user_id"
    )
    grouped_files = defaultdict(list)
    for row in files_objects:
        grouped_files[row.user_id].append(row.pk)

    for _, pk_list in grouped_files.items():
        inspect_users_files.delay(pk_list)


@shared_task
def inspect_users_files(key_list):
    objects_to_update = []
    result = []
    file_objects = UploadedFile.objects.filter(pk__in=key_list)

    for file in file_objects:
        try:
            result.append(check_style(file.file.path))
            objects_to_update.append(file)
        except Exception as ex:
            print("suka oshibka")
            print(ex)
    for i in result:
        print("pylint analiz")
        print(i[0])
        print("flake8 analiz")
        print(i[1])

    with transaction.atomic():
        objects_to_update = UploadedFile.objects.filter(
            pk__in=[obj.pk for obj in objects_to_update]
        )
        objects_to_update.update(inspected=True)

        log_objects_pk = []
        # Создание записи в логе для каждого обновленного объекта
        for obj, rez in zip(objects_to_update, result):
            log_objects_pk.append(
                InspectionLog.objects.create(
                    uploaded_file=obj,
                    message="inspected",
                    pylint_result=rez[0],
                    flake8_result=rez[1],
                ).pk
            )
        user = User.objects.get(pk=file_objects[0].user_id)
        print(log_objects_pk)
        mail_user.delay(user.email, log_objects_pk)
