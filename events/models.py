from django.db import models
from clients.models import Client
from contracts.models import Contract
from users.models import User


# Create your models here.
class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'support'})
    # todo check le event status foreignkey?
    # event_status = models.ForeignKey()
    attendees = models.IntegerField
    event_date = models.DateTimeField
    notes = models.TextField(max_length=2500)
