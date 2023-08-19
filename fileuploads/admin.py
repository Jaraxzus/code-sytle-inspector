from django.contrib import admin
from .models import InspectionLog, UploadedFile


@admin.register(InspectionLog)
class InspectionLogAdmin(admin.ModelAdmin):
    list_display = ("uploaded_file", "timestamp", "message", "user_notified")


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "file_name",
        "uploaded_at",
        "inspected",
    )
