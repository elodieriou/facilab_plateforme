import uuid
from django.db import models
from django.utils import timezone


class Test(models.Model):
    name = models.fields.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    second_updated = models.DateTimeField(auto_now=True)


"""class Applicant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.fields.CharField(max_length=128)
    last_name = models.fields.CharField(max_length=128)
    number_route = models.fields.CharField(max_length=10, blank=True, null=True)
    name_route = models.fields.CharField(max_length=255, blank=True, null=True)
    additional_address = models.fields.CharField(max_length=255, blank=True, null=True)
    postcode = models.fields.IntegerField(blank=True, null=True)
    city = models.fields.CharField(max_length=128, blank=True, null=True)
    phone = models.fields.CharField(max_length=10)
    mail = models.fields.CharField(max_length=128)
    password = models.fields.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id})"


class Prescriber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    type_organization = models.CharField(max_length=128)
    name_organization = models.CharField(max_length=128)
    number_route_organization = models.IntegerField(blank=True, null=True)
    name_route_organization = models.CharField(max_length=255, blank=True, null=True)
    additional_address_organization = models.CharField(max_length=255, blank=True, null=True)
    postcode_organization = models.IntegerField(blank=True, null=True)
    city_organization = models.CharField(max_length=128, blank=True, null=True)
    web_site = models.CharField(max_length=255)
    phone_organization = models.CharField(max_length=10)
    mail_organization = models.EmailField()
    password_organization = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name_organization} ({self.id})"


class Fablab(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    name_fablab = models.CharField(max_length=128)

    class Department(models.TextChoices):
        CALVADOS = '14'
        COTES_DARMOR = '22'
        FINISTERE = '29'
        ILE_ET_VILAINE = '35'
        LOIRE_ATLANTIQUE = '44'
        MAINE_ET_LOIRE = '49'
        MANCHE = '50'
        MAYENNE = '53'
        MORBIHAN = '56'
        ORNE = '61'
        SARTHE = '72'
        VENDEE = '85'

    department = models.fields.CharField(choices=Department.choices, max_length=50)
    presentation_fablab = models.TextField()
    skills_fablab = models.CharField(max_length=255)
    phone_fablab = models.CharField(max_length=10)
    mail_fablab = models.EmailField()
    password_fablab = models.CharField(max_length=125)

    def __str__(self):
        return f"{self.name_fablab} ({self.id})"
"""


class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    request_title = models.CharField(max_length=255, verbose_name='Titre')
    request_detail = models.TextField(verbose_name='Description')
    """applicant_id = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.SET_NULL)
    prescriber_id = models.ForeignKey(Prescriber, blank=True, null=True, on_delete=models.SET_NULL)"""

    def __str__(self):
        return f"{self.request_title} ({self.id})"


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
