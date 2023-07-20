from django.contrib import admin
from django.urls import path, include

from tenentpoc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('home', views.Home.as_view(), name='home'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('users', include('userapi.urls')),
    path('api-auth/', include('rest_framework.urls')),
]