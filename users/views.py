from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import DjangoModelPermissions
from users.permissions import ActualDjangoModelPermissions
from django.db.models import Q
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):

    permission_classes = [DjangoModelPermissions]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def get_object(self):
    #     obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
    #     self.check_object_permissions(self.request, obj)
    #
    # def perform_create(self, serializer):
    #     pass
    #
    # def perform_update(self, serializer):
    #     pass
    #
