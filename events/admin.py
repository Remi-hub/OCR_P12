from django.contrib import admin
from events.models import Event
from events.forms import EventForm


class EventAdmin(admin.ModelAdmin):
    form = EventForm

    def get_queryset(self, request):
        if request.user.groups.filter(name__iexact='management').exists():
            return Event.objects.all()

        elif request.user.groups.filter(name__iexact='sales').exists():
            return Event.objects.all()

        elif request.user.groups.filter(name__iexact='support').exists():
            return Event.objects.filter(support_contact=request.user)

    def has_change_permission(self, request, obj=None):

        if obj is not None and obj.status == "finished":
            if request.user.groups.filter(name__iexact='support').exists():
                return False

        if obj is not None and obj.client.sales_contact != request.user:
            return False
        return True

        # return super().has_change_permission(request, obj)


# Register your models here.
admin.site.register(Event, EventAdmin)
