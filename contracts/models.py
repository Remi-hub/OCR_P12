from django.db import models
from django.utils import timezone
import datetime
from clients.models import Client
from django.contrib.auth.models import User


# Create your models here.
class Contract(models.Model):

    def __str__(self):
        return f'Contract for the client {self.client}'

    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    amount = models.FloatField(default=0)
    payment_due = models.DateField(default=datetime.date.today)
    signed = models.BooleanField(default=False, verbose_name='Is the contract signed ?')
