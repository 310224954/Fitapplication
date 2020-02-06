from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegistrationForm

def registration_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("Home")
        else:
            form = RegistrationForm()

        context = {"form": form}
        return render(request, 'Users/registration.html', context)
        
    else:
        return redirect("Home")


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if next is not None:
                        return redirect("Home")
                    else:
                        return redirect("Home")
        else:
            form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'Users/login.html', context)
    else:
        return redirect("Home")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("Home")