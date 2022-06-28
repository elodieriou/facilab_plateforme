from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from plateform.models import Test, Request
from plateform.forms import RequestForm
from authentication.models import User


def test_django(request):
    tests = Test.objects.all()
    return render(request, 'test.html', {'tests': tests})


@login_required
def list_requests(request):
    list_of_request = Request.objects.all()
    return render(request, 'list_requests.html', {'requests': list_of_request})


def detail_request(request, id):
    detail_of_request = Request.objects.get(id=id)
    return render(request, 'detail_request.html', {'request': detail_of_request})

                  
"""def create_request(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        form = CreateRequestForm(request.POST)
        return redirect('list-request')
    else:
        form = CreateRequestForm()
    return render(request, 'create_request.html', {'form_request': form})"""


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


@login_required
def table_request(request):
    table_of_request = Request.objects.all()
    return render(request, 'table_request.html', {'requests': table_of_request})
