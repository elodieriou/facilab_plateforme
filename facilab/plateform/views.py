from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from plateform.models import Test, Request
from plateform.forms import RequestForm
from authentication.models import User, ApplicantUser


def test_django(request):
    tests = Test.objects.all()
    return render(request, 'test.html', {'tests': tests})


@login_required
def list_requests(request):
    list_of_request = Request.objects.filter(user=request.user)
    return render(request, 'list_requests.html', {'requests': list_of_request})


@login_required
def table_request(request):
    table_of_request = Request.objects.all()
    return render(request, 'table_request.html', {'requests': table_of_request})


@login_required
def detail_request(request, id):
    detail_of_request = Request.objects.get(id=id)
    user_search = User.objects.get(request=id)
    applicant_element = ApplicantUser.objects.get(user_id=user_search)
    return render(request, 'detail_request.html', {'request': detail_of_request,
                                                   'user_request': user_search,
                                                   'user_applicant': applicant_element})


@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return redirect('detail-request', new_request.id)
    else:
        form = RequestForm()
    return render(request, 'create_request.html', {'form': form})


class UpdateRequest(UpdateView):
    model = Request
    form_class = RequestForm
    template_name = 'update_request.html'

    def form_valid(self, form):
        request = form.save()
        return redirect('list-request')


class DeleteRequest(DeleteView):
    model = Request
    template_name = 'delete_request.html'
    success_url = reverse_lazy('list-request')


@login_required
def table_request(request):
    table_of_request = Request.objects.all()
    return render(request, 'table_request.html', {'requests': table_of_request})


"""def create_request(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        form = CreateRequestForm(request.POST)
        return redirect('list-request')
    else:
        form = CreateRequestForm()
    return render(request, 'create_request.html', {'form_request': form})"""


"""def detail_request(request, id):
    detail_of_request = Request.objects.get(id=id)
    user_element = Request.objects.filter(user__pk=7)
    element_search = User.objects.get(request=id)
    applicant_search = ApplicantUser.objects.get(user_id=element_search)
    id_user = element_search.id
    first_name = applicant_search.first_name
    last_name = applicant_search.last_name
    username = element_search.username
    print("id : {}".format(id))
    print("Detail of request : {}".format(detail_of_request))
    print("User element : {}".format(user_element))
    print("User for request (1) : {}".format(element_search))
    print("Id user : {}".format(id_user))
    print("first_name user : {}".format(first_name))
    print("last_name user : {}".format(last_name))
    print("username user : {}".format(username))
    return render(request, 'detail_request.html', {'request': detail_of_request, 'user': applicant_search})"""
