from django.contrib import admin
from contracts.models import Contract
from contracts.forms import ContractForm


# Register your models here.


class ContractAdmin(admin.ModelAdmin):
    form = ContractForm

    def get_queryset(self, request):
        if request.user.groups.filter(name__iexact='management').exists():
            return Contract.objects.all()

        elif request.user.groups.filter(name__iexact='sales').exists():
            return Contract.objects.all()

        if request.user.groups.filter(name__iexact='support').exists():
            return Contract.objects.all()

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.sales_contact != request.user:
            return False

        return True


admin.site.register(Contract, ContractAdmin)
