from django.urls import path, include
from rest_framework import routers

from .views import StudentViewSet

router = routers.SimpleRouter()
router.register('', StudentViewSet, basename="student")
urlpatterns = [
   path('student', include(router.urls)),
]