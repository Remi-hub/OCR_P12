from events.models import Event
from django.forms import ModelForm
from contracts.models import Contract
from django.db.models import Q
from django.contrib.auth.models import User, Permission, Group

support_permission = Group.objects.get(name='Support')
print(type(support_permission))

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contract'].queryset = Contract.objects.filter(Q(signed=True) & (Q(event__isnull=True) |
                                                                   Q(event=self.instance)))
        self.fields['support_contact'].queryset = User.objects.filter(groups=support_permission)
