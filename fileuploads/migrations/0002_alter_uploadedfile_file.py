# Generated by Django 4.2.4 on 2023-08-17 10:39

from django.db import migrations, models
import fileuploads.models


class Migration(migrations.Migration):
    dependencies = [
        ("fileuploads", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadedfile",
            name="file",
            field=models.FileField(upload_to=fileuploads.models.user_directory_path),
        ),
    ]
