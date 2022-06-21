from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.EmailField(label='Votre identifiant (adresse mail)')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Votre mot de passe')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input-line full-width'})
        self.fields['password'].widget.attrs.update({'class': 'input-line full-width'})


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['type_user', 'first_name', 'last_name',
                  'number_route', 'name_route', 'additional_address',
                  'postcode', 'city', 'phone_number', 'email']
