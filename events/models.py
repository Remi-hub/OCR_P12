from django.db import models
from django.utils import timezone

from clients.models import Client
# from users.models import User
from contracts.models import Contract
from django.contrib.auth.models import User
id = 1

EVENT_STATUS = (
    ("on_going", "On going"),
    ("finished", "Finished")
)


# Create your models here.
class Event(models.Model):

    def __str__(self):
        return f'{self.date_created} - Event for {self.client} '

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True) \
        if models.DateField(auto_now_add=True) is None \
        else models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField(choices=EVENT_STATUS)
    attendees = models.IntegerField(default=0)
    event_date = models.DateField(default=timezone.now)
    notes = models.TextField(max_length=2500, blank=True)
    # contract = models.ForeignKey(Contract, on_delete=models.CASCADE,
    #                              null=True, blank=True, limit_choices_to={'signed': 'True'})
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE,
                                    null=True, blank=True)

# todo possibilité de cacher les choix one to one deja créer
# todo ajouter systeme de login (users)
# todo substituer le model de base user de django par le notre

# associer un contract a un event, event vierge peut etre ?
# equipe de gestion = superusers django full CRUD
# equipe sales / support -> users personnalisé (avec restriction)
