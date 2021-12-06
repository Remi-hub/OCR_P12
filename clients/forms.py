from django.forms import ModelForm
from clients.models import Client
from django.contrib.auth.models import User


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sales_contact' in self.fields:
            self.fields['sales_contact'].queryset = User.objects.filter(groups__name='Sales')
