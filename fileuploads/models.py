from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    return f"uploads/user_{instance.user.id}/{filename}"


class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    inspected = models.BooleanField(default=False)
    # is_new = models.BooleanField(default=True)
    # is_overwritten = models.BooleanField(default=False)

    def __str__(self):
        return self.file.name
