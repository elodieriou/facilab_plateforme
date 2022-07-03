from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, UpdateView
from django.urls import reverse
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
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home-page')
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
        return redirect('list-request')


class SignupFablab(CreateView):
    model = User
    form_class = SignupFablabForm
    template_name = 'user_fablab.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('table-request')


def detail_profile(request, id):
    detail_of_profile = User.objects.get(id=id)
    applicant_element = ApplicantUser.objects.get(user_id=detail_of_profile)
    return render(request, 'detail_profile_applicant.html', {'user_profile': detail_of_profile,
                                                             'applicant_profile': applicant_element})


class UpdateProfileApplicant(UpdateView):
    model = User
    form_class = SignupApplicantForm
    template_name = 'update_profile_applicant.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('list-request')


"""def update_profile_applicant(request, id):
    user = User.objects.get(id=id)
    applicant_user = ApplicantUser.objects.get(user_id=user)
    if request.method == 'POST':
        user_form = LoginForm(request.POST, instance=user)
        applicant_form = SignupApplicantForm(request.POST, instance=applicant_user)

        if user_form.is_valid() and applicant_form.is_valid():
            user_form.save()
            applicant_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('list-request')
    else:
        user_form = LoginForm()
        applicant_form = SignupApplicantForm()

    return render(request, 'update_profile_applicant.html', {'user_form': user_form, 'applicant_form': applicant_form})"""







"""def update_profile(request, id):
    user = User.objects.get(id=id)

    if user.is_applicant is True:
        applicant = ApplicantUser.objects.get(user=id)
        if request.method == 'POST':
            applicant_form = SignupApplicantForm(request.POST, instance=applicant)
            if applicant_form.is_valid():
                applicant_form.save()
                return redirect('list-request', id=id)
        else:
            applicant_form = SignupApplicantForm(instance=request.applicant)
        return render(request, 'detail_profile_applicant.html', {'applicant': applicant_form})

    elif user.is_fablab is True:
        fablab = FablabUser.objects.get(user=id)
        if request.method == 'POST':
            fablab_form = SignupApplicantForm(request.POST, instance=fablab)
            if fablab_form.is_valid():
                fablab_form.save()
                return redirect('table-request', id=id)
        else:
            fablab_form = SignupFablabForm(instance=request.fablab)
        return render(request, 'update_profile_applicant.html', {'fablab': fablab_form})"""




"""class UpdateProfileApplicant(UpdateView):
    model = User
    form_class = SignupApplicantForm
    template_name = 'detail_profile_applicant.html'

    def form_valid(self, form_applicant):
        user = form_applicant.save()
        return redirect('list-request')


class UpdateProfileFablab(UpdateView):
    model = User
    form_class = SignupFablabForm
    template_name = 'update_profile_applicant.html'

    def form_valid(self, form_fablab):
        user = form_fablab.save()
        return redirect('table-request')"""
