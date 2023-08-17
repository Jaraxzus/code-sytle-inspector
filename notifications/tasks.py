from celery import shared_task
from code_style_inspector import settings
from django.core.mail import send_mail


@shared_task
def mail_user(recipient):
    subject = "Files inspected"
    message = "Files incpected check your filelist"
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [recipient])
