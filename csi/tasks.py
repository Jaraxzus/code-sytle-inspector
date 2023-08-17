from collections import defaultdict
from celery import shared_task
from csi.utils import check_style
from fileuploads.models import UploadedFile


@shared_task
def inspection():
    files_objects = UploadedFile.objects.filter(inspected=False).order_by(
        "user_id"
    )
    grouped_files = defaultdict(list)
    for row in files_objects:
        grouped_files[row.user_id].append(row.pk)

    for _, pk_list in grouped_files.items():
        inspect_users_files(pk_list)


@shared_task
def inspect_users_files(key_list):
    objects_to_update = []
    result = []
    file_objects = UploadedFile.objects.filter(pk__in=key_list)

    for file in file_objects:
        try:
            # print(file.__dict__)
            result.append(check_style(file.file.path))
            objects_to_update.append(file)
        except Exception as ex:
            print("suka oshibka")
            print(ex)
    for i in result:
        print(i[0])
        print(i[1])

    UploadedFile.objects.filter(
        pk__in=[obj.pk for obj in objects_to_update]
    ).update(**{"inspected": True})
