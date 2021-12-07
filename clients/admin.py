from django.contrib import admin
from clients.models import Client
from clients.forms import ClientForm


class ClientAdmin(admin.ModelAdmin):
    form = ClientForm

    def get_queryset(self, request):
        if 'Management' in request.user.groups.all().values_list("name", flat=True):
            return Client.objects.all()

        elif 'Sales' in request.user.groups.all().values_list("name", flat=True):
            return Client.objects.all()

        elif 'Support' in request.user.groups.all().values_list("name", flat=True):
            return Client.objects.filter(events__support_contact=request.user)


# Register your models here.
admin.site.register(Client, ClientAdmin)
