from django.contrib.auth import login
from django.shortcuts import render, redirect

# from .forms import CustomUserCreationForm
#
#
# def register(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(
#                 "home"
#             )  # Замените 'home' на имя вашей домашней страницы
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "registration/register.html", {"form": form})
