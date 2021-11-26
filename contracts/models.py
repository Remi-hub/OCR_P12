from django.db import models
from django.utils import timezone

from clients.models import Client
# from users.models import User
from django.contrib.auth.models import User

CONTRACT_STATUS = (
    ("on_going", "On going"),
    ("finished", "Finished")
)


# Create your models here.
class Contract(models.Model):

    def __str__(self):
        return f'Contract for the client {self.client}'

    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True) \
        if models.DateTimeField(auto_now_add=True) is None\
        else models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    amount = models.FloatField(default=0)
    payment_due = models.DateField(default=timezone.now)
    signed = models.BooleanField(default=False, verbose_name='Is the contract signed ?')


# todo ajouter field en booleen true ou false
# todo vraiment besoin de status ?