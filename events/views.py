from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from events.models import Event
from events.serializers import EventSerializer



class EventViewSet(viewsets.ModelViewSet):

    permission_classes = [DjangoModelPermissions]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
