from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenent(TenantMixin):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True
    auto_drop_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
