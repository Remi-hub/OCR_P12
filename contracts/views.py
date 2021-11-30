from rest_framework import viewsets
from contracts.models import Contract
from rest_framework.permissions import DjangoModelPermissions
from contracts.serializers import ContractSerializer


# Create your views here.
class ContractViewSet(viewsets.ModelViewSet):

    permission_classes = [DjangoModelPermissions]
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
