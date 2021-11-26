from django.db import models
from django.contrib.auth.models import User





# ROLE = (
#     ('management', 'management'),
#     ('sales', 'sales'),
#     ('support', 'support')
# )
#
#
# # Create your models here.
# class User(models.Model):
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name} from the team {self.role}'
#
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     role = models.TextField(choices=ROLE)
