from django.contrib import admin
from events.models import Event
from events.forms import EventForm


class EventAdmin(admin.ModelAdmin):
    form = EventForm

    def get_queryset(self, request):
        if 'Management' in request.user.groups.all().values_list("name", flat=True):
            return Event.objects.all()

        elif 'Sales' in request.user.groups.all().values_list("name", flat=True):
            return Event.objects.all()

        elif 'Support' in request.user.groups.all().values_list("name", flat=True):
            return Event.objects.filter(support_contact=request.user)


# Register your models here.
admin.site.register(Event, EventAdmin)
