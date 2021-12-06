from contracts.models import Contract
from django.forms import ModelForm
from django.db.models import Q
from django.contrib.auth.models import User, Group


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sales_contact'].queryset = User.objects.filter(groups__name='Sales')
