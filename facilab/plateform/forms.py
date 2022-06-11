from django import forms
from plateform.models import Request


"""class CreateRequestForm(forms.Form):
    titre = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)"""


class RequestForm(forms.ModelForm):
    class Meta:
        """This class define the model use for the form"""
        model = Request
        fields = '__all__'
