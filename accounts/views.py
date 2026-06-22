from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages as ms
from django.contrib.auth import authenticate, login, logout
from home.models import *

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        users = User.objects.all()
        if form.is_valid():
            cd = form.cleaned_data
            for user in users:
                if str(cd['Username']) == str(user):
                    ms.error(request, "Username already exists")
                    return redirect("register")
                elif str(cd['Email']) == str(user.email):
                    ms.error(request, "Email already registered")
                    return redirect("register")

            User.objects.create_user(cd['Username'], cd['Email'], cd['Password'])
            authenticated_user = authenticate(request, username=form.cleaned_data['Username'], password=form.cleaned_data['Password'])
            login(request, authenticated_user)
            Status.objects.create(accountid=authenticated_user)
            Customization.objects.create(accountid=authenticated_user)
            ms.success(request, "Account created successfully")
            Chats.objects.all().filter(accountid=authenticated_user).delete()
            return redirect("homepage")

    else:
        form = UserRegisterForm()
    return render(request, "forms/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            authenticated_user = authenticate(request, username=form.cleaned_data['Username'], password=form.cleaned_data['Password'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                ms.success(request, "Logged in successfully")
                return redirect("homepage")
            else:
                ms.error(request, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, "forms/login.html", {"form": form})

def user_logout(request):
    logout(request)
    ms.success(request, "Successfully logged out")
    return redirect("homepage")

def delete_account(request):
    if request.method == "POST":
        DeletePassword = request.POST.get('DeletePassword')
        DelAccAuth = authenticate(request, username=request.user, password=DeletePassword)
        if DelAccAuth is not None:
            a = User.objects.get(username=request.user.username)
            a.is_active = False
            a.save()
            ms.success(request, "Account deleted successfully")
        else:
            ms.error(request, "Wrong password")
        return redirect("homepage")