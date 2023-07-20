from rest_framework.permissions import BasePermission
from django_tenants.utils import get_public_schema_name


class IsPublicSchemaSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                if request.tenant.schema_name == get_public_schema_name():
                    return True
        return False

