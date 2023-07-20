from django.urls import path, include
from rest_framework import routers
from superadmin.views import SuperAdminTenantViewsSet, SuperAdminStudentViewsSet


router = routers.SimpleRouter()

router.register('tenants', SuperAdminTenantViewsSet, basename="superadmin-tenants")
router.register('students', SuperAdminStudentViewsSet, basename="superadmin-students")
urlpatterns = [
    path('', include(router.urls)),
]
