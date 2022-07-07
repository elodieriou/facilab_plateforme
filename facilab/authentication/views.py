"""This module defines some classes and functions that send HTTP response
or HTML templating render"""
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, UpdateView
from django.urls import reverse_lazy
from authentication.forms import SignupApplicantForm, SignupFablabForm
from authentication.forms import LoginForm
from authentication.models import User, ApplicantUser, FablabUser


class LoginPage(View):
    """This class defines the view login page"""
    form_class = LoginForm()
    template_name = 'login.html'

    def get(self, request):
        """This method overrides the http get request"""
        form = self.form_class
        message = ''
        return render(request, self.template_name,
                      context={'form': form, 'message': message})

    def post(self, request):
        """This method overrides the http post request"""
        form = LoginForm(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home-page')
            else:
                message = "Identifiants invalides."
        return render(request, self.template_name,
                      context={'form': form, 'message': message})


def logout_user(request):
    """This function defines the logout process"""
    logout(request)
    return redirect('login')


def user_type(request):
    """This function defines the view of choosing profile"""
    return render(request, 'user_type.html')


class SignupApplicant(CreateView):
    """This class defines the signup applicant view"""
    model = User
    form_class = SignupApplicantForm
    template_name = 'user_applicant.html'

    def form_valid(self, form):
        """This method defines the process if the form is valid"""
        user = form.save()
        login(self.request, user)
        return redirect('list-request')


class SignupFablab(CreateView):
    """This class defines the signup fablab view"""
    model = User
    form_class = SignupFablabForm
    template_name = 'user_fablab.html'

    def form_valid(self, form):
        """This method defines the process if the form is valid"""
        user = form.save()
        login(self.request, user)
        return redirect('table-request')


def detail_profile(request, id):
    """This function defines the show profile view"""
    detail_of_profile = User.objects.get(id=id)
    applicant_element = ApplicantUser.objects.get(user_id=detail_of_profile)
    return render(request, 'detail_profile_applicant.html',
                  {'user_profile': detail_of_profile, 'applicant_profile': applicant_element})


def update_profile(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = SignupApplicantForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('profile-applicant', user.id)
    else:
        form = SignupApplicantForm(instance=user)
    return render(request, 'update_profile_applicant.html', {'form': form})


"""class UpdateProfileApplicant(UpdateView):
    model = User
    form_class = SignupApplicantForm
    template_name = 'update_profile_applicant.html'
    success_url = reverse_lazy('profile-applicant', model.id)

    def get_object(self):
        return self.request.user"""
