from django import forms
from plateform.models import Request


class RequestForm(forms.ModelForm):
    """This class define the request form to apply"""
    class Meta:
        """This class define the model use for the form"""
        model = Request
        fields = ['request_title', 'request_detail']


"""class CreateRequestForm(forms.Form):
    titre = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)"""
