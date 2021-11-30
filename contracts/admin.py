from django.contrib import admin
from contracts.models import Contract
from contracts.forms import ContractForm

# Register your models here.


class ContractAdmin(admin.ModelAdmin):
    form = ContractForm


admin.site.register(Contract, ContractAdmin)
