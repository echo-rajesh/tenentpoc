from rest_framework import serializers

from tenent.models import Tenent


class TenentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenent
        fields = ('id', 'name', 'address', 'created_on')
