from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Domain, Tenent


class DomainInline(admin.TabularInline):
    model = Domain
    max_num = 1


@admin.register(Tenent)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "created_on",
    )
    inlines = [DomainInline]
