from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    return f"uploads/user_{instance.user.id}/{filename}"


class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    inspected = models.BooleanField(default=False)

    def __str__(self):
        return self.file.name


class InspectionLog(models.Model):
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    massage = models.CharField(max_length=50)
    pylint_result = models.TextField(default="")
    flake8_result = models.TextField(default="")

    def __str__(self):
        return f"Log for {self.uploaded_file}"
