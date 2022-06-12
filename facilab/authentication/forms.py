from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Votre identifiant (adresse mail)')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Votre mot de passe')
