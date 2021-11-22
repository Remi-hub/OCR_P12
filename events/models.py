from django.db import models
from django.utils import timezone

from clients.models import Client
from contracts.models import Contract
from users.models import User
import datetime

EVENT_STATUS = (
    ("on_going", "On going"),
    ("finished", "Finished")
)


# Create your models here.
class Event(models.Model):

    def __str__(self):
        return f'Event for the client {self.client}'

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True) \
        if models.DateTimeField(auto_now_add=True) is None\
        else models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'support'})
    status = models.TextField(choices=EVENT_STATUS)
    attendees = models.IntegerField(default=0)
    event_date = models.DateField(default=timezone.now)
    notes = models.TextField(max_length=2500)

