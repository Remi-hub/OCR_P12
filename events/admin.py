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
            return Event.objects.all()

    def has_change_permission(self, request, obj=None):

        # can't modify event if user is from support and event is finished
        if obj is not None and obj.status == "finished":
            if request.user.groups.filter(name__iexact='support').exists():
                return False

        # can't modify event if user is from sales and is not the sales contact
        elif request.user.groups.filter(name__iexact="sales").exists():
            if obj is not None and obj.client.sales_contact != request.user:
                return False
        # can't modify if user from support is not the support contact
        elif request.user.groups.filter(name__iexact="support").exists():
            if obj is not None and obj.support_contact != request.user:
                return False

        return super().has_change_permission(request, obj)


# Register your models here.
admin.site.register(Event, EventAdmin)
