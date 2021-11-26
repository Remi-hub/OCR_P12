from django.contrib import admin
from events.models import Event
from events.forms import EventForm


class EventAdmin(admin.ModelAdmin):
  form = EventForm

# Register your models here.
admin.site.register(Event, EventAdmin)