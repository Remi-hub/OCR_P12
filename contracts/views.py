from rest_framework import viewsets
from contracts.models import Contract
from OCR_P12.permissions import ActualDjangoModelPermissions, PermissionContract
from contracts.serializers import ContractSerializer


# Create your views here.
class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = [ActualDjangoModelPermissions, PermissionContract]
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
