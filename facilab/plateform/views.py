"""This module defines some classes and functions that send HTTP response
or HTML templating render"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from plateform.models import Request
from plateform.forms import RequestForm
from authentication.models import User, ApplicantUser


@login_required
def home_page(request):
    """This function define the home page view"""
    return render(request, 'home_page.html')


@login_required
def list_requests(request):
    """This function defines the list of request for one user"""
    list_of_request = Request.objects.filter(user=request.user)
    return render(request, 'list_requests.html', {'requests': list_of_request})


@login_required
def table_request(request):
    """This function defines the list of all request for the fablab profile"""
    table_of_request = Request.objects.all()
    return render(request, 'table_request.html', {'requests': table_of_request})


@login_required
def table_request_fablab(request):
    """This function defines the list of all request for the fablab profile"""
    table_of_request = Request.objects.all()
    return render(request, 'table_request_fablab.html', {'requests': table_of_request})


@login_required
def detail_request_list_applicant(request, id):
    """This function defines the show request view"""
    detail_of_request = Request.objects.get(id=id)
    user_search = User.objects.get(request=id)
    applicant_element = ApplicantUser.objects.get(user_id=user_search)
    return render(request, 'detail_request_list_applicant.html',
                  {'request': detail_of_request,
                   'user_request': user_search,
                   'user_applicant': applicant_element})


@login_required
def detail_request_table_applicant(request, id):
    """This function defines the show request view"""
    detail_of_request = Request.objects.get(id=id)
    user_search = User.objects.get(request=id)
    applicant_element = ApplicantUser.objects.get(user_id=user_search)
    return render(request, 'detail_request_table_applicant.html',
                  {'request': detail_of_request,
                   'user_request': user_search,
                   'user_applicant': applicant_element})


@login_required()
def detail_request_fablab(request, id):
    detail_of_request = Request.objects.get(id=id)
    user_search = User.objects.get(request=id)
    applicant_element = ApplicantUser.objects.get(user_id=user_search)
    return render(request, 'detail_request_fablab.html', {'request': detail_of_request,
                                                          'user_request': user_search,
                                                          'user_applicant': applicant_element})


@login_required
def create_request(request):
    """This function defines the create request view"""
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return redirect('detail-request-list-applicant', new_request.id)
    else:
        form = RequestForm()
    return render(request, 'create_request.html', {'form': form})


class UpdateRequest(UpdateView):
    """This class defines the update request view"""
    model = Request
    form_class = RequestForm
    template_name = 'update_request.html'

    def form_valid(self, form):
        """This method define the process if the form is valid"""
        request = form.save()
        return redirect('list-request')


class DeleteRequest(DeleteView):
    """This class defines the delete request view"""
    model = Request
    template_name = 'delete_request.html'
    success_url = reverse_lazy('list-request')
