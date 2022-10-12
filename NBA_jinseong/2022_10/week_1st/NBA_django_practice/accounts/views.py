from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render('accounts/index.html', users)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())

            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)

    return redirect('accounts:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }

    return render(request, 'accounts/update.html', context)

def delete(request):
    request.user.delete()
    auth_logout(request)

    return redirect('accounts:index')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }

    return render(request, 'accounts/change_password.html', context)

