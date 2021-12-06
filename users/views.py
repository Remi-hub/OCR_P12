from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import DjangoModelPermissions
from OCR_P12.permissions import ActualDjangoModelPermissions
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):

    permission_classes = [ActualDjangoModelPermissions]
    serializer_class = UserSerializer
    queryset = User.objects.all()
