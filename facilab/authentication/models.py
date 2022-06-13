from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    APPLICANT = 'APPLICANT'
    PRESCRIBER = 'PRESCRIBER'
    FABLAB = 'FABLAB'

    TYPE_USERS = (
        (APPLICANT, 'Demandeur'),
        (PRESCRIBER, 'Prescripteur'),
        (FABLAB, 'FabLab')
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    type_user = models.CharField(max_length=20, choices=TYPE_USERS, verbose_name='Qui suis-je ?')
    first_name = models.fields.CharField(max_length=128, verbose_name='Prénom')
    last_name = models.fields.CharField(max_length=128, verbose_name='Nom')
    number_route = models.fields.CharField(max_length=10, blank=True, null=True, verbose_name='N° de voie')
    name_route = models.fields.CharField(max_length=255, blank=True, null=True, verbose_name='Nom de voie')
    additional_address = models.fields.CharField(max_length=255, blank=True, null=True, verbose_name='Complément d\'adresse')
    postcode = models.fields.IntegerField(blank=True, null=True, verbose_name='Code postal')
    city = models.fields.CharField(max_length=128, blank=True, null=True, verbose_name='Ville')
    phone_number = models.fields.CharField(max_length=10, verbose_name='Téléphone')

