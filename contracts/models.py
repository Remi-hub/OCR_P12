from django.db import models
from django.utils import timezone

from clients.models import Client
from users.models import User


CONTRACT_STATUS = (
    ("on_going", "On going"),
    ("finished", "Finished")
)


# Create your models here.
class Contract(models.Model):

    def __str__(self):
        return f'Contract for the client {self.client}, status is : {self.status}'

    sales_contact = models.ForeignKey(User, limit_choices_to={"role": 'sales'}, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True) \
        if models.DateTimeField(auto_now_add=True) is None\
        else models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=CONTRACT_STATUS)
    amount = models.FloatField(default=0)
    payment_due = models.DateField(default=timezone.now)
