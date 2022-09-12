"""This module defines the models that define the database"""
from django.db import models
from django.utils import timezone
from authentication.models import User


CATEGORIE_CHOICES = [
    ('Aides techniques', 'Aides techniques'),
    ('Aides technologiques', 'Aides technologiques'),
    ('Aides domotiques', 'Aides domotiques'),
    ('Gabarits', 'Gabarits')
]

MATIERE_CHOICES = [
    ('Pas de matière prédéfinie', 'Pas de matière prédéfinie'),
    ('Textile', 'Textile'),
    ('Métal', 'Métal'),
    ('Plastique', 'Plastique'),
    ('Bois', 'Bois')
]

CONTRAINTE_CHOICES = [
    ('Pas de contrainte identifiée', 'Pas de contrainte identifiée'),
    ('Normes alimentaires', 'Normes alimentaires')
]


class Request(models.Model):
    """This class define the table Request"""
    id = models.AutoField(
        primary_key=True)
    created_at = models.DateTimeField(
        default=timezone.now)
    updated_at = models.DateTimeField(
        auto_now=True)
    request_title = models.CharField(
        max_length=255,
        verbose_name='Titre')
    request_detail = models.TextField(
        verbose_name='Description')
    categorie = models.CharField(
        choices=CATEGORIE_CHOICES,
        max_length=55,
        verbose_name='Catégorie')
    matiere = models.CharField(
        choices=MATIERE_CHOICES,
        max_length=55,
        verbose_name='Matière')
    contrainte = models.CharField(
        choices=CONTRAINTE_CHOICES,
        max_length=55,
        verbose_name='Contrainte')
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        """The method str render more readable the object Request"""
        return f"{self.request_title} ({self.id})"


class Response(models.Model):
    """This class define the table Response"""
    id = models.AutoField(
        primary_key=True)
    created_at = models.DateTimeField(
        default=timezone.now)
    updated_at = models.DateTimeField(
        auto_now=True)
    comment = models.TextField(
        verbose_name='Commentaire')
    request_id = models.ForeignKey(
        Request,
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        """The method str render more readable the object Response"""
        return f"{self.id}, {self.comment}"


"""class Response(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    first_name_leader_project = models.CharField(max_length=125)
    last_name_leader_project = models.CharField(max_length=125)
    phone_leader_project = models.CharField(max_length=10)
    mail_leader_project = models.EmailField()
    comment = models.TextField()
    fablab_id = models.ForeignKey(Fablab, null=True, on_delete=models.SET_NULL)
    request_id = models.ForeignKey(Request, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name_leader_project} {self.last_name_leader_project} of {self.fablab_id}"
"""
