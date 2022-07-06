"""This module display the models in the django admin panel."""
from django.contrib import admin
from authentication.models import User, ApplicantUser, FablabUser


class UserAdmin(admin.ModelAdmin):
    """This class defines the models for user table in the django admin
     panel"""
    list_display = ('id',
                    'username',
                    'password',
                    'created_at',
                    'updated_at')


class ApplicantAdmin(admin.ModelAdmin):
    """This class defines the models for user applicant table in the django
     admin panel"""
    list_display = ('id',
                    'first_name',
                    'last_name')


class FablabAdmin(admin.ModelAdmin):
    """This class defines the models for user fablab table in the django
     admin panel"""
    list_display = ('id',
                    'name')


admin.site.register(User, UserAdmin)
admin.site.register(ApplicantUser, ApplicantAdmin)
admin.site.register(FablabUser, FablabAdmin)
