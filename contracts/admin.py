from django.contrib import admin
from contracts.models import Contract
from contracts.forms import ContractForm


# Register your models here.


class ContractAdmin(admin.ModelAdmin):
    form = ContractForm

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.sales_contact != request.user:
            return False
        return True


admin.site.register(Contract, ContractAdmin)
