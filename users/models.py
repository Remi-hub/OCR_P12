from django.db import models


ROLE = (
    ('management', 'management'),
    ('sales', 'sales'),
    ('support', 'support')
)


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    role = models.TextField(choices=ROLE)
