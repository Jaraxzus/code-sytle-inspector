from code_style_inspector import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("upload/", views.upload_file, name="upload_file"),
    path("files/", views.file_list, name="file_list"),
    path("delete/<int:file_id>/", views.delete_file, name="delete_file"),
    path("file_detail/<int:file_id>/", views.file_detail, name="file_detail"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
