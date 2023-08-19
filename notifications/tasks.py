from celery import shared_task
from code_style_inspector import settings
from django.core.mail import send_mail
from django.db import transaction

from fileuploads.models import InspectionLog


@shared_task
def mail_user(recipient, log_objects_pk):
    subject = "Files inspected"
    message = "Files incpected check your filelist"
    from_email = settings.EMAIL_HOST_USER
    try:
        send_mail(subject, message, from_email, [recipient])
        with transaction.atomic():
            objects_to_update = InspectionLog.objects.filter(
                pk__in=log_objects_pk
            )
            objects_to_update.update(user_notified=True)
    except Exception as ex:
        print(ex)
