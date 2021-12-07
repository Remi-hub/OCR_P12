from events.models import Event
from django.forms import ModelForm
from contracts.models import Contract
from django.db.models import Q
from django.contrib.auth.models import User, Group


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('hello')
        # if 'Management' in self.request.user.groups.all().values_list("name", flat=True):
        #     pass
        #
        # elif 'Sales' in self.request.user.groups.all().values_list("name", flat=True):
        #     pass
        #
        # elif 'Support' in self.request.user.groups.all().values_list("name", flat=True):
        #     pass

        self.fields['contract'].queryset = Contract.objects.filter(Q(signed=True) & (Q(event__isnull=True) |
                                                                                     Q(event=self.instance)))
        self.fields['support_contact'].queryset = User.objects.filter(groups__name='Support')
