"""This module contains a registry of installed applications that store
configuration and provides introspection"""
from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """This class defines the configuration of the authentication app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
