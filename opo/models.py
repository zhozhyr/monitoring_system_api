from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

"""
Опасные объекты и надзор
"""


class BaseDirectory(models.Model):
    """
    Базовый абстрактный класс для справочников.
    """
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название")

    class Meta:
        abstract = True


class TypeOPO(BaseDirectory):
    """
    Модель для хранения информации о типах ОПО
    """
    short_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Краткое название")
    reg_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Регистрационный номер")

    class Meta:
        verbose_name = "Тип ОПО"
        verbose_name_plural = "Типы ОПО"

    def __str__(self):
        return self.name or self.reg_number or str(self.id)


class OPO(models.Model):
    """
    Модель для хранения информации об ОПО
    """
    id = models.BigIntegerField(primary_key=True, verbose_name="ID ОПО")
    type = models.ForeignKey(TypeOPO, on_delete=models.CASCADE, verbose_name="ID типа ОПО")
    structural_unit = models.IntegerField(verbose_name="ID структурного подразделения")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название")
    short_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Краткое название")
    reg_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="Регистрационный номер")

    class Meta:
        verbose_name = "ОПО"
        verbose_name_plural = "ОПО"

    def __str__(self):
        return self.reg_number or self.name or str(self.id)


class HazardClass(BaseDirectory):
    """
    Модель, представляющая класс опасности.
    Используется для классификации опасных объектов.
    """

    class Meta:
        verbose_name = "Класс опасности"
        verbose_name_plural = "Классы опасности"

    def __str__(self):
        return self.name if self.name else "Класс опасности (без названия)"
