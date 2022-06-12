from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from authentication.forms import LoginForm


def logout_user(request):
    logout(request)
    return redirect('login')


def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                """message = f"Vous êtes connecté !"""
                return redirect('list-request')
            else:
                message = "Identifiants invalides."
    return render(request, 'login.html', context={'form': form, 'message': message})

