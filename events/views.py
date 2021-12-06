from rest_framework import viewsets
from OCR_P12.permissions import ActualDjangoModelPermissions
from events.models import Event
from events.serializers import EventSerializer



class EventViewSet(viewsets.ModelViewSet):

    permission_classes = [ActualDjangoModelPermissions]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
