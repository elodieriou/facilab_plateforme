"""This module defines forms base on models"""
from django import forms
from plateform.models import Request, Response


class RequestForm(forms.ModelForm):
    """This class define the request form to apply"""
    class Meta:
        """This class define the model use for the form"""
        model = Request
        fields = ['request_title', 'request_detail', 'categorie', 'matiere', 'contrainte']


class ResponseForm(forms.ModelForm):
    """This class define the repsonse for to apply"""
    class Meta:
        """This class define the model use for the form"""
        model = Response
        fields = ['comment']
