from django.contrib import admin
from clients.models import Client
from clients.forms import ClientForm


class ClientAdmin(admin.ModelAdmin):
    form = ClientForm


# Register your models here.
admin.site.register(Client, ClientAdmin)
