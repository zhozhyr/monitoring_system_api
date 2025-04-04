from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import serializers, viewsets, permissions, mixins
from rest_framework.views import APIView

from .models import OPO, HazardClass, TypeOPO
from .serializers import (OPOSerializer,
                          HazardClassSerializer, TypeOPOSerializer, )
from .decorators import schema_view


class BaseDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = ['id', 'name']


DIRECTORY_MODELS = {
    'hazard_class': HazardClass,
    'type_opo': TypeOPO,
}


@schema_view("Справочники ОПО")
@extend_schema(
    parameters=[
        OpenApiParameter(
            name='directory_type',
            description='Тип справочника',
            required=True,
            type=str,
            enum=list(DIRECTORY_MODELS.keys()),
            location=OpenApiParameter.PATH
        )
    ],
    responses=HazardClassSerializer(many=True)
)
class DirectoryView(APIView):
    def get(self, request, directory_type):
        Model = DIRECTORY_MODELS.get(directory_type)
        if not Model:
            raise NotFound("Неизвестный справочник")
        queryset = Model.objects.all()

        serializer_class = {
            'hazard_class': HazardClassSerializer,
            'type_opo': TypeOPOSerializer,
        }.get(directory_type, None)

        if serializer_class is None:
            raise NotFound("Сериализатор не найден")

        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='directory_type',
            description='Тип справочника',
            required=True,
            type=str,
            enum=list(DIRECTORY_MODELS.keys()),
            location=OpenApiParameter.PATH
        ),
    ],
    responses=HazardClassSerializer  # это пример, можно динамически
)
@schema_view("Справочники ОПО")
class DirectoryDetailView(APIView):
    def get(self, request, directory_type, pk):
        Model = DIRECTORY_MODELS.get(directory_type)
        if not Model:
            raise NotFound("Неизвестный справочник")

        obj = get_object_or_404(Model, pk=pk)

        serializer_class = {
            'hazard_class': HazardClassSerializer,
            'type_opo': TypeOPOSerializer,
        }.get(directory_type)

        if serializer_class is None:
            raise NotFound("Сериализатор не найден")

        serializer = serializer_class(obj)
        return Response(serializer.data)


@schema_view('ОПО')
class OPOViewSet(viewsets.ModelViewSet):
    queryset = OPO.objects.all()
    serializer_class = OPOSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
