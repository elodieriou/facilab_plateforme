"""This module defines the models that define the database"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """This class define the table User"""
    is_applicant = models.BooleanField(default=False)
    is_fablab = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """The method str render more readable the object User"""
        return f"{self.username} ({self.pk})"


class ApplicantUser(models.Model):
    """This class define the model Applicant base on the model User"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.fields.CharField(
        max_length=128,
        verbose_name='Prénom')
    last_name = models.fields.CharField(
        max_length=128,
        verbose_name='Nom')
    number_route = models.fields.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='N° de voie')
    name_route = models.fields.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Nom de voie')
    additional_address = models.fields.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Complément d\'adresse')

    class Department(models.TextChoices):
        """This class define the list of departments"""
        CALVADOS = '14', '14 - Calvados'
        COTES_DARMOR = '22', '22 - Côtes d\'armor'
        FINISTERE = '29', '29 - Finistère'
        ILE_ET_VILAINE = '35', '35 - Ile-et-Vilaine'
        LOIRE_ATLANTIQUE = '44', '44 - Loire Atlantique'
        MAINE_ET_LOIRE = '49', '49 - Maine-et-Loire'
        MANCHE = '50', '50 - Manche'
        MAYENNE = '53', '53 - Mayenne'
        MORBIHAN = '56', '56 - Morbihan'
        ORNE = '61', '61 - Orne'
        SARTHE = '72', '72 - Sarthe'
        VENDEE = '85', '85 - Vendée'

    department = models.fields.CharField(
        choices=Department.choices,
        max_length=50)
    postcode = models.fields.CharField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name='Code postal')
    city = models.fields.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='Ville')
    type_organization = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='Type d\'organisation')
    name_organization = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='Nom de l\'organisation')
    web_site = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Site internet')
    phone_number = models.fields.CharField(
        max_length=10,
        verbose_name='Téléphone')

    def __str__(self):
        """The method str render more readable the object User Applicant"""
        return f"{self.first_name} {self.last_name} ({self.pk})"


class FablabUser(models.Model):
    """This class define the model Fablab base on the model User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=128,
        verbose_name='Nom du FabLab')
    presentation = models.TextField(
        max_length=255,
        verbose_name='Présentation')

    class Department(models.TextChoices):
        """This class define the list of departments"""
        CALVADOS = '14', '14 - Calvados'
        COTES_DARMOR = '22', '22 - Côtes d\'armor'
        FINISTERE = '29', '29 - Finistère'
        ILE_ET_VILAINE = '35', '35 - Ile-et-Vilaine'
        LOIRE_ATLANTIQUE = '44', '44 - Loire Atlantique'
        MAINE_ET_LOIRE = '49', '49 - Maine-et-Loire'
        MANCHE = '50', '50 - Manche'
        MAYENNE = '53', '53 - Mayenne'
        MORBIHAN = '56', '56 - Morbihan'
        ORNE = '61', '61 - Orne'
        SARTHE = '72', '72 - Sarthe'
        VENDEE = '85', '85 - Vendée'

    department = models.fields.CharField(
        choices=Department.choices,
        max_length=50)
    phone_number = models.fields.CharField(
        max_length=10,
        verbose_name='Téléphone')
    number_route = models.fields.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='N° de voie')
    name_route = models.fields.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Nom de voie')
    additional_address = models.fields.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Complément d\'adresse')
    postcode = models.fields.CharField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name='Code postal')
    city = models.fields.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='Ville')
    web_site = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Site internet')

    def __str__(self):
        """The method str render more readable the object User Applicant"""
        return f"{self.name} ({self.pk})"
