from rest_framework import viewsets
from clients.serializers import ClientSerializer
from clients.models import Client
from OCR_P12.permissions import ActualDjangoModelPermissions


# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [ActualDjangoModelPermissions]
    serializer_class = ClientSerializer

    def get_queryset(self):
        if 'Management' in self.request.user.groups.all().values_list("name", flat=True):
            return Client.objects.all()

        elif 'Sales' in self.request.user.groups.all().values_list("name", flat=True):
            return Client.objects.all()

        elif 'Support' in self.request.user.groups.all().values_list("name", flat=True):
            return Client.objects.filter(events__support_contact=self.request.user).distinct()
