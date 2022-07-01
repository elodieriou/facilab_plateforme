from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User, ApplicantUser, FablabUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Votre identifiant')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Votre mot de passe')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-line full-width'})
        self.fields['password'].widget.attrs.update({'class': 'input-line full-width'})


DEPARTMENTS = [('14', '14 - Calvados'),
               ('22', '22 - Côtes d\'armor'),
               ('29', '29 - Finistère'),
               ('35', '35 - Ile-et-Vilaine'),
               ('44', '44 - Loire Atlantique'),
               ('49', '49 - Maine-et-Loire'),
               ('50', '50 - Manche'),
               ('53', '53 - Mayenne'),
               ('56', '56 - Morbihan'),
               ('61', '61 - Orne'),
               ('72', '72 - Sarthe'),
               ('85', '85 - Vendée')]


class SignupApplicantForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='Identifiant *')
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        label='Mot de passe *')
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        label='Confirmer le mot de passe *')
    first_name = forms.CharField(
        required=True,
        label='Prénom *')
    last_name = forms.CharField(
        required=True,
        label='Nom *')
    phone_number = forms.CharField(
        required=True,
        label='Téléphone *')
    department = forms.ChoiceField(
        required=True,
        widget=forms.Select,
        choices=DEPARTMENTS,
        label='Département *')
    number_route = forms.CharField(
        required=False,
        label='N° de voie')
    name_route = forms.CharField(
        required=False,
        label='Nom de voie')
    additional_address = forms.CharField(
        required=False,
        label='Complément d\'adresse')
    postcode = forms.CharField(
        required=False,
        label='Code postal')
    city = forms.CharField(
        required=False,
        label='Ville')
    type_organization = forms.CharField(
        required=False,
        label='Type d\'organisation')
    name_organization = forms.CharField(
        required=False,
        label='Nom de l\'organisation')
    web_site = forms.CharField(
        required=False,
        label='Site internet')

    username.widget.attrs.update({'class': 'input-line full-width'})
    password1.widget.attrs.update({'class': 'input-line full-width'})
    password2.widget.attrs.update({'class': 'input-line full-width'})
    first_name.widget.attrs.update({'class': 'input-line full-width'})
    last_name.widget.attrs.update({'class': 'input-line full-width'})
    phone_number.widget.attrs.update({'class': 'input-line full-width'})
    department.widget.attrs.update({'class': 'input-line full-width special-area'})
    number_route.widget.attrs.update({'class': 'input-line full-width'})
    name_route.widget.attrs.update({'class': 'input-line full-width'})
    additional_address.widget.attrs.update({'class': 'input-line full-width'})
    postcode.widget.attrs.update({'class': 'input-line full-width'})
    city.widget.attrs.update({'class': 'input-line full-width'})
    type_organization.widget.attrs.update({'class': 'input-line full-width'})
    name_organization.widget.attrs.update({'class': 'input-line full-width'})
    web_site.widget.attrs.update({'class': 'input-line full-width'})

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        """This function overwrite the method save and the decorator
        permits not to add data error in database."""
        user = super().save(commit=False)
        user.is_applicant = True
        user.save()
        applicant = ApplicantUser.objects.create(user=user)
        applicant.first_name = self.cleaned_data.get('first_name')
        applicant.last_name = self.cleaned_data.get('last_name')
        applicant.phone_number = self.cleaned_data.get('phone_number')
        applicant.department = self.cleaned_data.get('department')
        applicant.number_route = self.cleaned_data.get('number_route')
        applicant.name_route = self.cleaned_data.get('name_route')
        applicant.additional_address = self.cleaned_data.get('additional_address')
        applicant.postcode = self.cleaned_data.get('postcode')
        applicant.city = self.cleaned_data.get('city')
        applicant.type_organization = self.cleaned_data.get('type_organization')
        applicant.name_organization = self.cleaned_data.get('name_organisation')
        applicant.web_site = self.cleaned_data.get('web_site')
        applicant.save()
        return user


class SignupFablabForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='Identifiant *')
    password1 = forms.CharField(
        required=True,
        label='Mot de passe *')
    password2 = forms.CharField(
        required=True,
        label='Confirmer le mot de passe *')
    name = forms.CharField(
        required=True,
        label='Nom du FabLab *')
    presentation = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label='Présentation *')
    phone_number = forms.CharField(
        required=True,
        label='Téléphone *')
    department = forms.ChoiceField(
        required=True,
        widget=forms.Select,
        choices=DEPARTMENTS,
        label='Département *')
    web_site = forms.CharField(
        required=False,
        label='Site internet')
    number_route = forms.CharField(
        required=False,
        label='N° de voie')
    name_route = forms.CharField(
        required=False,
        label='Nom de voie')
    additional_address = forms.CharField(
        required=False,
        label='Complément d\'adresse')
    postcode = forms.CharField(
        required=False,
        label='Code postal')
    city = forms.CharField(
        required=False,
        label='Ville')

    username.widget.attrs.update({'class': 'input-line full-width'})
    password1.widget.attrs.update({'class': 'input-line full-width'})
    password2.widget.attrs.update({'class': 'input-line full-width'})
    name.widget.attrs.update({'class': 'input-line full-width'})
    presentation.widget.attrs.update({'class': 'input-line full-width special-area'})
    phone_number.widget.attrs.update({'class': 'input-line full-width'})
    department.widget.attrs.update({'class': 'input-line full-width special-area'})
    number_route.widget.attrs.update({'class': 'input-line full-width'})
    name_route.widget.attrs.update({'class': 'input-line full-width'})
    additional_address.widget.attrs.update({'class': 'input-line full-width'})
    postcode.widget.attrs.update({'class': 'input-line full-width'})
    city.widget.attrs.update({'class': 'input-line full-width'})
    web_site.widget.attrs.update({'class': 'input-line full-width'})

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        """This function overwrite the method save and the decorator
        permits not to add data error in database."""
        user = super().save(commit=False)
        user.is_fablab = True
        user.save()
        fablab = FablabUser.objects.create(user=user)
        fablab.name = self.cleaned_data.get('name')
        fablab.presentation = self.cleaned_data.get('presentation')
        fablab.phone_number = self.cleaned_data.get('phone_number')
        fablab.department = self.cleaned_data.get('department')
        fablab.number_route = self.cleaned_data.get('number_route')
        fablab.name_route = self.cleaned_data.get('name_route')
        fablab.additional_address = self.cleaned_data.get('additional_address')
        fablab.postcode = self.cleaned_data.get('postcode')
        fablab.city = self.cleaned_data.get('city')
        fablab.web_site = self.cleaned_data.get('web_site')
        fablab.save()
        return user
