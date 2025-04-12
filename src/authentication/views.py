from django.urls import reverse
from .forms import RegisterForm
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def register_view(request):
    context = {}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = CustomUser.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect(reverse("home"))
    else:
        form = RegisterForm()

    context["form"] = form
    return render(request, "register_form.html", context)



def login_view(request):
    context = {}

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("home"))
            else:
                context["error"] = "Неверный логин или пароль."
    else:
        form = LoginForm()

    context["form"] = form
    return render(request, "login_form.html", context)

def logout_view(request):
    logout(request)
    return redirect(reverse("home"))
