"""This module contains a registry of installed applications that store
configuration and provides introspection"""
from django.apps import AppConfig


class PlateformConfig(AppConfig):
    """This class defines the configuration of the plateform app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plateform'
