from rest_framework import serializers
from .models import OPO, HazardClass, TypeOPO


class BaseDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']


class TypeOPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOPO
        fields = ['id', 'name', 'short_name', 'reg_number']


class HazardClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = HazardClass
        fields = ['id', 'name']


class OPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPO
        fields = ['id', 'name', 'reg_number']
