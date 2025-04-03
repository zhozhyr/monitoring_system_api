from rest_framework import serializers
from .models import (
    TU, Certificate, ControlNote,
    Manufacturer, NameTU, KindTU, TypeTU
)
from opo.serializers import OPOSerializer, HazardClassSerializer


class BaseDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ['id', 'name']


class ManufacturerSerializer(BaseDirectorySerializer):
    class Meta(BaseDirectorySerializer.Meta):
        model = Manufacturer
        fields = ['id', 'name', 'country']


class NameTUSerializer(BaseDirectorySerializer):
    class Meta(BaseDirectorySerializer.Meta):
        model = NameTU


class KindTUSerializer(BaseDirectorySerializer):
    class Meta(BaseDirectorySerializer.Meta):
        model = KindTU
        fields = ['id', 'name', 'is_for_journal']


class TypeTUSerializer(BaseDirectorySerializer):
    class Meta(BaseDirectorySerializer.Meta):
        model = TypeTU
        fields = ['id', 'name', 'is_for_journal']


class TUSerializer(serializers.ModelSerializer):
    manufacturer_id = ManufacturerSerializer(read_only=True)
    device_name_id = NameTUSerializer(read_only=True)
    device_type_id = TypeTUSerializer(read_only=True)
    kind_device_id = KindTUSerializer(read_only=True)
    hazard_class_id = HazardClassSerializer(read_only=True)
    opo_id = OPOSerializer(read_only=True)

    class Meta:
        model = TU
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    tu = TUSerializer(read_only=True)

    class Meta:
        model = Certificate
        fields = '__all__'


class ControlNoteSerializer(serializers.ModelSerializer):
    tu = TUSerializer(read_only=True)

    class Meta:
        model = ControlNote
        fields = '__all__'
