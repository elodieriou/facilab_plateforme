from django.contrib import admin
from authentication.models import User, ApplicantUser, FablabUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'username',
                    'password',
                    'created_at',
                    'updated_at')


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'first_name',
                    'last_name')


class FablabAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name')


admin.site.register(User, UserAdmin)
admin.site.register(ApplicantUser, ApplicantAdmin)
admin.site.register(FablabUser, FablabAdmin)
