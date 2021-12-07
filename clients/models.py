from django.db import models
from django.contrib.auth.models import User

CLIENT_STATUS = (
    ("prospect", "prospect"),
    ("acquired", "acquired")
)


# Create your models here.
class Client(models.Model):

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    """
    fields that contains informations about the client
    """
    first_name = models.CharField(max_length=25, verbose_name='First name')
    last_name = models.CharField(max_length=25, verbose_name='Last name')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True) \
        if models.DateTimeField(auto_now_add=True) is None \
        else models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField(default="potential", choices=CLIENT_STATUS)
