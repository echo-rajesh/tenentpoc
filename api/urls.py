from django.urls import path, include

urlpatterns = [
    path('v1/', include('school.urls')),
    path('v1/superadmin/', include('superadmin.urls')),
]
