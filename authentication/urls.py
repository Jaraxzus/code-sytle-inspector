from django.urls import include, path
from . import views


urlpatterns = [
    # path(""),
    path("", include("django.contrib.auth.urls")),
    # path("register/", views.register, name="register"),
]
