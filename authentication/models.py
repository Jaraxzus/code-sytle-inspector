from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.utils.regex_helper import Group


# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     # Добавьте related_name для groups и user_permissions
#     groups = models.ManyToManyField(
#         Group, blank=True, related_name="custom_users"
#     )
#     user_permissions = models.ManyToManyField(
#         Permission, blank=True, related_name="custom_users"
#     )
