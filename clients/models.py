from django.db import models
from contracts.models import Contract
from users.models import User


# Create your models here.
class Client(models.Model):
    """
    fields that contains informations about the client
    """
    first_name = models.CharField(max_length=25, verbose_name='First name')
    last_name = models.CharField(max_length=25, verbose_name='Last name')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"role": 'sales'})
