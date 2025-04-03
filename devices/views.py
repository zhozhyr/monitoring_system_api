from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import serializers, viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .models import (
    TU, Certificate, ControlNote,
    Manufacturer, NameTU, KindTU, TypeTU
)
from .serializers import (ManufacturerSerializer,
                          NameTUSerializer, KindTUSerializer,
                          TypeTUSerializer, TUSerializer,
                          CertificateSerializer, ControlNoteSerializer, BaseDirectorySerializer)
from .decorators import schema_view

DIRECTORY_MODELS = {
    'manufacturer': Manufacturer,
    'name_tu': NameTU,
    'kind_tu': KindTU,
    'type_tu': TypeTU,
}



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
    responses=NameTUSerializer(many=True)
)
@schema_view("Справочники ТУ")
class DirectoryView(APIView):
    def get(self, request, directory_type):
        Model = DIRECTORY_MODELS.get(directory_type)
        if not Model:
            raise NotFound("Неизвестный справочник")
        queryset = Model.objects.all()

        serializer_class = {
            'manufacturer': ManufacturerSerializer,
            'name_tu': NameTUSerializer,
            'kind_tu': KindTUSerializer,
            'type_tu': TypeTUSerializer
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
    responses=NameTUSerializer
)
@schema_view("Справочники ТУ")
class DirectoryDetailView(APIView):
    def get(self, request, directory_type, pk):
        Model = DIRECTORY_MODELS.get(directory_type)
        if not Model:
            raise NotFound("Неизвестный справочник")

        obj = get_object_or_404(Model, pk=pk)

        serializer_class = {
            'manufacturer': ManufacturerSerializer,
            'name_tu': NameTUSerializer,
            'kind_tu': KindTUSerializer,
            'type_tu': TypeTUSerializer
        }.get(directory_type)

        if serializer_class is None:
            raise NotFound("Сериализатор не найден")

        serializer = serializer_class(obj)
        return Response(serializer.data)


@schema_view('Тех.устройства')
class TUViewSet(viewsets.ModelViewSet):
    queryset = TU.objects.all()
    serializer_class = TUSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


@schema_view('Заметки')
class ControlNoteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = ControlNoteSerializer

    def get_queryset(self):
        tu_pk = self.kwargs.get("tu_pk")
        if tu_pk:
            return ControlNote.objects.filter(tu_id=tu_pk)
        return ControlNote.objects.none()  # или self.queryset

    def perform_create(self, serializer):
        tu = get_object_or_404(TU, pk=self.kwargs["tu_pk"])
        serializer.save(tu=tu)


@schema_view('Сертификаты')
class CertificateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
