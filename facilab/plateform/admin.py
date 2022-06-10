from django.contrib import admin
from plateform.models import Test, Applicant, Prescriber, Fablab, Response, Request


class TestAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'date',
                    'updated',
                    'second_updated')


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'first_name',
                    'last_name',
                    'phone',
                    'mail',
                    'password',
                    'created_at',
                    'updated_at')


class PrescriberAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name_organization',
                    'web_site',
                    'phone_organization',
                    'mail_organization',
                    'password_organization',
                    'created_at',
                    'updated_at')


class FablabAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name_fablab',
                    'department',
                    'created_at',
                    'updated_at')


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'first_name_leader_project',
                    'last_name_leader_project',
                    'comment',
                    'created_at',
                    'updated_at')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'request_title',
                    'created_at',
                    'updated_at')


admin.site.register(Test, TestAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Prescriber, PrescriberAdmin)
admin.site.register(Fablab, FablabAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Request, RequestAdmin)
