"""This module display the models in the django admin panel."""
from django.contrib import admin
from plateform.models import Request


class RequestAdmin(admin.ModelAdmin):
    """This class defines the models for request table in the django admin
    panel"""
    list_display = ('id',
                    'request_title',
                    'created_at',
                    'updated_at')


admin.site.register(Request, RequestAdmin)
