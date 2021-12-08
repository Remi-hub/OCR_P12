from contracts.models import Contract
from django.forms import ModelForm
from django.contrib.auth.models import User
from clients.models import Client


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sales_contact' in self.fields:
            self.fields['sales_contact'].queryset = User.objects.filter(groups__name='Sales')
            self.fields['client'].queryset = Client.objects.filter(status='acquired')
