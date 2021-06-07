from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from .models import User

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                return redirect('index-url')
    return render(request, 'login.html', {'form': form})


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    phone_number=form.cleaned_data['phone_number'],
                    password=form.cleaned_data['password']
                )
                login(request, user)
                return redirect('index-url')
            except Exception as e:
                pass
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login-url')
