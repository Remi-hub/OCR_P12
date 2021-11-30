from rest_framework.permissions import DjangoModelPermissions


class ActualDjangoModelPermissions(DjangoModelPermissions):
    view_permissions = ['%(OCR_P12)s.view_%(User)s']

    perms_map = {
        'GET': view_permissions,
        'OPTIONS': view_permissions,
        'HEAD': view_permissions,
        'POST': DjangoModelPermissions.perms_map['POST'],
        'PUT': DjangoModelPermissions.perms_map['PUT'],
        'PATCH': DjangoModelPermissions.perms_map['PATCH'],
        'DELETE': DjangoModelPermissions.perms_map['DELETE'],
    }
