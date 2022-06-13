from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from authentication.forms import LoginForm, SignupForm


class LoginPage(View):
    form_class = LoginForm()
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = LoginForm(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                """message = f"Vous êtes connecté !"""
                return redirect('list-request')
            else:
                message = "Identifiants invalides."
        return render(request, self.template_name, context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_URL)
    return render(request, 'signup.html', context={'form': form})
