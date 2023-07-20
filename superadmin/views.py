from django_tenants.utils import schema_context
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404

from school.serializers import StudentSerializer
from .permissions import IsPublicSchemaSuperUser
from rest_framework.response import Response
from school.models import Student

from tenent.models import Tenent
from tenent.serializers import TenentSerializer


class SuperAdminTenantViewsSet(viewsets.ViewSet):
    permission_classes = [IsPublicSchemaSuperUser]

    def list(self, request):
        queryset = Tenent.objects.all()
        serializer = TenentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TenentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        queryset = Tenent.objects.all()
        tenant = get_object_or_404(queryset, pk=pk)
        serializer = TenentSerializer(tenant)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Tenent.objects.all()
        tenant = get_object_or_404(queryset, pk=pk)
        serializer = TenentSerializer(tenant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        queryset = Tenent.objects.all()
        tenant = get_object_or_404(queryset, pk=pk)
        tenant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SuperAdminStudentViewsSet(viewsets.ModelViewSet):
    permission_classes = [IsPublicSchemaSuperUser]
    
    def list(self, request):
        print("Inside list")
        with schema_context(request.GET.get('schema_name')):
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
