from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.conf import settings
from authentication.forms import LoginForm, SignupApplicantForm, SignupFablabForm
from authentication.models import User, ApplicantUser, FablabUser


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


def user_type(request):
    return render(request, 'user_type.html')


class SignupApplicant(CreateView):
    model = User
    form_class = SignupApplicantForm
    template_name = 'user_applicant.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('create-request')


class SignupFablab(CreateView):
    model = User
    form_class = SignupFablabForm
    template_name = 'user_fablab.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('list-request')
