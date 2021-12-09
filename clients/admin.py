from django.contrib import admin
from clients.models import Client
from clients.forms import ClientForm


class ClientAdmin(admin.ModelAdmin):
    form = ClientForm

    def get_queryset(self, request):
        if request.user.groups.filter(name__iexact='management').exists():
            return Client.objects.all()

        elif request.user.groups.filter(name__iexact='sales').exists():
            return Client.objects.all()
        
        # old queryset for clients
        # elif request.user.groups.filter(name__iexact='support').exists():
        #     return Client.objects.filter(events__support_contact=request.user)

        elif request.user.groups.filter(name__iexact='support').exists():
            return Client.objects.all()

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.sales_contact != request.user:
            return False
        return True


# Register your models here.
admin.site.register(Client, ClientAdmin)
