from django.contrib.auth.models import User
from rest_framework.permissions import DjangoModelPermissions, BasePermission
from contracts.models import Contract
from clients.models import Client


class ActualDjangoModelPermissions(DjangoModelPermissions):

    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['HEAD'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['OPTIONS'] = ['%(app_label)s.view_%(model_name)s']


class PermissionEvent(BasePermission):

    def has_object_permission(self, request, view, obj):

        if obj is not None and obj.status == "finished":
            if request.user.groups.filter(name__iexact='support').exists():
                return False

        if request.user.groups.filter(name__iexact="sales").exists() and obj.client.sales_contact != request.user:
            return False

        if obj is not None and obj.support_contact != request.user:
            return False

        return super().has_object_permission(request, view, obj)


class PermissionClient(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name__iexact="sales").exists() and obj.sales_contact != request.user:
            return False
        return True


class PermissionContract(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name__iexact="sales").exists() and obj.sales_contact != request.user:
            return False
        return True
