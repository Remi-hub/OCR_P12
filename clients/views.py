from rest_framework import viewsets
from clients.serializers import ClientSerializer
from clients.models import Client
from OCR_P12.permissions import ActualDjangoModelPermissions


# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):

    permission_classes = [ActualDjangoModelPermissions]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
