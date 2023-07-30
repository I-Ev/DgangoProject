from django.contrib import admin

from mailing.models import MailingSetting, Email, Client


@admin.register(MailingSetting)
class MailingSettingAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'periodicity', 'status']


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['subject', 'body', 'mailing_setting']


@admin.register(Client)
class ClientlAdmin(admin.ModelAdmin):
    list_display = ['name', 'patrony', 'surname', 'email', 'comment']
