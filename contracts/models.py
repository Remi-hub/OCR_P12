from django.db import models
from clients.models import Client
from users.models import User


CONTRACT_STATUS = (
    ("on_going", "On going"),
    ("finished", "Finished")
)


# Create your models here.
class Contract(models.Model):
    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField
    date_updated = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=CONTRACT_STATUS)
    amount = models.FloatField
    payment_due = models.DateTimeField
