from rest_framework import viewsets
from clients.serializers import ClientSerializer
from clients.models import Client
from rest_framework.permissions import DjangoModelPermissions


# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):

    permission_classes = [DjangoModelPermissions]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
