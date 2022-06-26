class SignupApplicantForm(forms.Form):
    class Meta:
        model = ApplicantUser
        fields = ['first_name', 'last_name', 'phone_number',
                  'type_organisation', 'name_organization', 'web_site',
                  'number_route', 'name_route', 'additional_address',
                  'department', 'postcode', 'city',
                  'username', 'password']


"""class SignupFablabFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['name_fablab', 'presentation_fablab', 'skills_fablab',
                  'number_route', 'name_route', 'additional_address',
                  'department', 'postcode', 'city',
                  'username', 'password']"""


"""A mettre dans models.py"""
class Skills(models.TextChoices):
    SKILLS_1 = '1', 'Catégorie 1'
    SKILLS_2 = '2', 'Catégorie 2'
    SKILLS_3 = '3', 'Catégorie 3'


skills = models.CharField(
    max_length=20,
    choices=Skills,
    default=Skills.SKILLS_1,
    verbose_name='Catégorie')


"""A mettre dans forms.py"""
LIST_SKILLS = [('1', 'Catégorie 1'), ('2', 'Catégorie 2'), ('3', 'Catégorie 3')]


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    is_applicant = models.BooleanField(default=False)
    is_fablab = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class UserType(models.TextChoices):
        APPLICANT = 'APPLICANT', 'Applicant'
        FABLAB = 'FABLAB', 'Fablab'
        ADMIN = 'ADMIN', 'Admin'

    type_user = models.CharField(max_length=20, choices=UserType.choices)
    number_route = models.fields.CharField(max_length=10, blank=True, null=True, verbose_name='N° de voie')
    name_route = models.fields.CharField(max_length=255, blank=True, null=True, verbose_name='Nom de voie')
    additional_address = models.fields.CharField(max_length=255, blank=True, null=True,
                                                 verbose_name='Complément d\'adresse')
    postcode = models.fields.IntegerField(blank=True, null=True, verbose_name='Code postal')
    city = models.fields.CharField(max_length=128, blank=True, null=True, verbose_name='Ville')

    def __str__(self):
        return f"{self.username} {self.type_user} ({self.pk})"


class ApplicantUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.fields.CharField(max_length=128, verbose_name='Prénom')
    last_name = models.fields.CharField(max_length=128, verbose_name='Nom')

    class Department(models.TextChoices):
        CALVADOS = '14', 'Calvados'
        COTES_DARMOR = '22', 'Côtes d\'armor'
        FINISTERE = '29', 'Finistère'
        ILE_ET_VILAINE = '35', 'Ile-et-Vilaine'
        LOIRE_ATLANTIQUE = '44', 'Loire Atlantique'
        MAINE_ET_LOIRE = '49', 'Maine-et-Loire'
        MANCHE = '50', 'Manche'
        MAYENNE = '53', 'Mayenne'
        MORBIHAN = '56', 'Morbihan'
        ORNE = '61', 'Orne'
        SARTHE = '72', 'Sarthe'
        VENDEE = '85', 'Vendée'

    department = models.fields.CharField(choices=Department.choices, max_length=50)
    type_organization = models.CharField(max_length=128, blank=True, null=True,
                                         verbose_name='Type d\'organisation')
    name_organization = models.CharField(max_length=128, blank=True, null=True,
                                         verbose_name='Nom de l\'organisation')
    web_site = models.CharField(max_length=255, blank=True, null=True,
                                verbose_name='Web site')
    phone_number = models.fields.CharField(max_length=10, verbose_name='Téléphone')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.pk})"


class ApplicantManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.UserType.APPLICANT)


class Applicant(User):
    objects = ApplicantManager()
    base_type = User.UserType.APPLICANT

    @property
    def more(self):
        return self.applicantmore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type_user = User.UserType.APPLICANT
        return super().save(*args, **kwargs)


class FablabUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_fablab = models.CharField(max_length=128, verbose_name='Nom du FabLab')
    presentation_fablab = models.TextField(verbose_name='Présentation')
    skills_fablab = models.CharField(max_length=255, verbose_name='Domaine de compétences')

    class Department(models.TextChoices):
        CALVADOS = '14', 'Calvados'
        COTES_DARMOR = '22', 'Côtes d\'armor'
        FINISTERE = '29', 'Finistère'
        ILE_ET_VILAINE = '35', 'Ile-et-Vilaine'
        LOIRE_ATLANTIQUE = '44', 'Loire Atlantique'
        MAINE_ET_LOIRE = '49', 'Maine-et-Loire'
        MANCHE = '50', 'Manche'
        MAYENNE = '53', 'Mayenne'
        MORBIHAN = '56', 'Morbihan'
        ORNE = '61', 'Orne'
        SARTHE = '72', 'Sarthe'
        VENDEE = '85', 'Vendée'

    department = models.fields.CharField(choices=Department.choices, max_length=50)
    phone_number = models.fields.CharField(max_length=10, verbose_name='Téléphone')

    def __str__(self):
        return f"{self.name_fablab} ({self.pk})"


class FablabManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.UserType.FABLAB)


class Fablab(User):
    objects = FablabManager()
    base_type = User.UserType.FABLAB

    @property
    def more(self):
        return self.fablabmore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type_user = User.UserType.FABLAB
        return super().save(*args, **kwargs)
