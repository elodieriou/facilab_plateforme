from django.http import HttpResponse
from django.shortcuts import render
from plateform.models import Test


def test_django(request):
    tests = Test.objects.all()
    return render(request, 'test.html', {'tests': tests})


def sign_in(request):
    return HttpResponse('<h1>Page de connection</h1>')


def sign_up(request):
    return HttpResponse('<h1>Créer un compte</h1> <p>Voi comment gérer les 3 profils</p>')


def list_request(request):
    return HttpResponse('<h1>Liste des demandes</h1>')


def create_request(request):
    return HttpResponse('<h1>Créer une demande</h1>')


def answer_request(request):
    return HttpResponse('<h1>Répondre à une demande</h1>')

