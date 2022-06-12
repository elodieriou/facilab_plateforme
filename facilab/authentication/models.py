from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    APPLICANT = 'APPLICANT'
    PRESCRIBER = 'PRESCRIBER'
    FABLAB = 'FABLAB'

    TYPE_USERS = (
        (APPLICANT, 'Demandeur'),
        (PRESCRIBER, 'Prescripteur'),
        (FABLAB, 'FabLab')
    )

    type_user = models.CharField(max_length=20, choices=TYPE_USERS, verbose_name='Qui suis-je ?')
