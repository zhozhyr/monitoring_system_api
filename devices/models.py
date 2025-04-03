from django.db import models
from opo.models import OPO, HazardClass

"""
Технические устройства (ТУ) и связанные данные
"""


class BaseDirectory(models.Model):
    """
    Базовый абстрактный класс для справочников.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название")

    class Meta:
        abstract = True


class Manufacturer(BaseDirectory):
    """
    Модель для хранения информации о заводах-изготовителях
    """
    country = models.CharField(max_length=200, null=True, blank=True, verbose_name="Страна-производитель")

    class Meta:
        verbose_name = "Завод-изготовитель"
        verbose_name_plural = "Заводы-изготовители"

    def __str__(self):
        return self.name or str(self.id)


class NameTU(BaseDirectory):
    """
    Модель для хранения информации о наименованиях тех. устройств.
    """

    class Meta:
        verbose_name = "Название ТУ"
        verbose_name_plural = "Названия ТУ"

    def __str__(self):
        return self.name or str(self.id)


class KindTU(BaseDirectory):
    """
    Модель для хранения информации о видах тех. устройств.
    """
    is_for_journal = models.BooleanField(default=False, verbose_name="Для журнала")

    class Meta:
        verbose_name = "Вид ТУ"
        verbose_name_plural = "Виды ТУ"

    def __str__(self):
        return self.name or str(self.id)


class TypeTU(BaseDirectory):
    """
    Модель для хранения информации о типах тех. устройств.
    """
    is_for_journal = models.BooleanField(default=False, verbose_name="Для журнала")

    class Meta:
        verbose_name = "Тип ТУ"
        verbose_name_plural = "Типы ТУ"

    def __str__(self):
        return self.name or str(self.id)


class TU(models.Model):
    """
    Модель технического устройства с основными характеристиками, идентификаторами,
    параметрами эксплуатации и документами.
    """
    # YES_NO_CHOICES = [
    #     (0, "Нет"),
    #     (1, "Да"),
    # ]

    # Основные сведения
    registration_number = models.CharField(max_length=200, null=True, blank=True,
                                           verbose_name="Регистрационный номер оборудования")
    serial_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Серийный номер")
    state_registration_number = models.CharField(max_length=200, null=True, blank=True,
                                                 verbose_name="Гос. регистрационный номер")
    factory_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Заводской номер")
    brand = models.CharField(max_length=500, null=True, blank=True, verbose_name="Марка")
    technical_characteristics = models.CharField(max_length=200, null=True, blank=True,
                                                 verbose_name="Краткие тех. характеристики")

    # Идентификация и схема
    gtt_registration_number = models.CharField(max_length=200, null=True, blank=True,
                                               verbose_name="Регистрационный номер ГТТ")
    scheme_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Номер по тех. схеме")

    # Годы эксплуатации
    manufacture_year = models.CharField(max_length=200, null=True, blank=True, verbose_name="Год изготовления")
    service_life_years = models.SmallIntegerField(null=True, blank=True,
                                                  verbose_name="Нормативный срок эксплуатации (лет)")
    commissioning_year = models.SmallIntegerField(null=True, blank=True, verbose_name="Год ввода в эксплуатацию")
    decommissioning_year = models.SmallIntegerField(null=True, blank=True, verbose_name="Год окончания эксплуатации")

    # Техническое состояние
    wear_percentage = models.FloatField(null=True, blank=True, verbose_name="Процент износа")
    last_epb_date = models.DateField(null=True, blank=True, verbose_name="Дата последнего ЭПБ")
    next_epb_date = models.DateField(null=True, blank=True, verbose_name="Дата следующего ЭПБ")
    last_inspection_date = models.DateField(null=True, blank=True, verbose_name="Дата очередной проверки")
    next_inspection_date = models.DateField(null=True, blank=True, verbose_name="Дата следующей проверки")
    permitted_service_life = models.SmallIntegerField(null=True, blank=True,
                                                      verbose_name="Разрешённый срок эксплуатации")

    # Предохранительные устройства
    has_safety_device = models.BooleanField(null=True, blank=True,
                                            verbose_name="Наличие предохранительного устройства")
    safety_device_type = models.CharField(max_length=200, null=True, blank=True,
                                          verbose_name="Тип предохранительного устройства")

    # Параметры оборудования
    volume_m3 = models.FloatField(null=True, blank=True, verbose_name="Объём (м³)")
    object_pressure_mpa = models.FloatField(null=True, blank=True, verbose_name="Объектное давление (МПа)")
    dy_mm = models.FloatField(null=True, blank=True, verbose_name="Диаметр (мм)")
    type = models.CharField(max_length=200, null=True, blank=True, verbose_name="Тип")
    subtype = models.CharField(max_length=200, null=True, blank=True, verbose_name="Подтип")
    lifting_capacity_t = models.FloatField(null=True, blank=True, verbose_name="Грузоподъёмность (т)")
    volume_t = models.FloatField(null=True, blank=True, verbose_name="Объём (т)")
    equipment_pressure_mpa = models.FloatField(null=True, blank=True, verbose_name="Давление оборудования (МПа)")
    modernization_year = models.SmallIntegerField(null=True, blank=True, verbose_name="Год модернизации")
    completed_measures = models.CharField(max_length=200, null=True, blank=True, verbose_name="Проведённые мероприятия")

    # Документы и разрешения
    rtn_permission_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Номер разрешения РТН")
    epb_conclusion_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Номер заключения ЭПБ")

    passport_present = models.BooleanField(null=True, blank=True,
                                           verbose_name="Наличие паспорта")

    opo_info = models.CharField(max_length=200, null=True, blank=True, verbose_name="Сведения об ОПО")

    rtn_info = models.BooleanField(null=True, blank=True, verbose_name="Информация РТН")

    compliance_certificate_present = models.BooleanField(null=True, blank=True,
                                                         verbose_name="Наличие сертификата соответствия")
    rtn_certificate_present = models.BooleanField(null=True, blank=True,
                                                  verbose_name="Наличие сертификата РТН")

    # Изготовитель
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True,
                                        verbose_name="ID завода-изготовителя")

    manufacturer_country = models.CharField(max_length=200, null=True, blank=True,
                                            verbose_name="Страна-производитель")
    manufacturer_name = models.CharField(max_length=500, null=True, blank=True, verbose_name="Завод-изготовитель")

    # Прочее
    epb_conclusion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Вывод ЭПБ")
    total_cycles = models.IntegerField(null=True, blank=True, verbose_name="Количество циклов")
    actual_cycles = models.IntegerField(null=True, blank=True, verbose_name="Фактическое количество циклов")
    replacement_id = models.IntegerField(null=True, blank=True, verbose_name="ID замены")
    replacement_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Номер замены")
    note1 = models.TextField(null=True, blank=True, verbose_name="Примечание 1")
    note2 = models.TextField(null=True, blank=True, verbose_name="Примечание 2")
    note3 = models.TextField(null=True, blank=True, verbose_name="Примечание 3")

    # Идентификаторы
    opo_id = models.ForeignKey(OPO, on_delete=models.CASCADE, verbose_name="ID ОПО")
    hazard_class_id = models.ForeignKey(HazardClass, on_delete=models.CASCADE, null=True, blank=True,
                                        verbose_name="ID класса опасности")
    device_type_id = models.ForeignKey(TypeTU, on_delete=models.CASCADE, null=True, blank=True,
                                       verbose_name="ID типа устройства")

    device_name_id = models.ForeignKey(NameTU, on_delete=models.CASCADE, verbose_name="ID наименования устройства")
    # rtn_id = models.IntegerField(null=True, blank=True, verbose_name="ID РТН") #что это?

    kind_device_id = models.ForeignKey(KindTU, on_delete=models.CASCADE, verbose_name="ID вида устройства")

    # kind_device_j_id = models.IntegerField(null=True, blank=True, verbose_name="ID вида устройства (J)")
    # type_device_j_id = models.IntegerField(null=True, blank=True, verbose_name="ID типа устройства (J)")

    # Контроль
    sr_control_presence_id = models.IntegerField(null=True, blank=True, verbose_name="ID наличия СР контроля")
    cb_oncontrol = models.BooleanField(default=0, verbose_name="На контроле")  # ?

    # Обновления
    date_updated = models.DateTimeField(null=True, blank=True, verbose_name="Дата обновления")
    updated_by = models.CharField(max_length=100, null=True, blank=True, verbose_name="Обновлено пользователем")
    is_deleted = models.BooleanField(default=0, verbose_name="Удалено")

    class Meta:
        verbose_name = "Техническое устройство"
        verbose_name_plural = "Технические устройства"

    def __str__(self):
        return self.brand or self.registration_number or str(self.id)


class Certificate(models.Model):
    """
    Модель для хранения информации о сертификате ТУ
    """
    type = models.CharField(max_length=500, verbose_name="Тип сертификата")
    number = models.CharField(max_length=200, verbose_name="Номер сертификата")
    date_from = models.DateField(null=True, blank=True, verbose_name="Дата выдачи")
    date_to = models.DateField(null=True, blank=True, verbose_name="Дата окончания")
    issued_by = models.CharField(max_length=500, verbose_name="Кем выдано")
    tu = models.ForeignKey(TU, null=True, on_delete=models.CASCADE, verbose_name="ID ТУ")
    scan = models.BinaryField(null=True, blank=True, verbose_name="Скан-копия")

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.number or str(self.id)


class ControlNote(models.Model):
    """
    Модель для хранения заметок контроля.
    Содержит текст заметки, дату создания и связанную информацию.
    """
    tu = models.ForeignKey(TU, on_delete=models.CASCADE, null=True, blank=True,
                           verbose_name="ID технического устройства")
    auto_card_number = models.IntegerField(null=True, blank=True, verbose_name="Номер карты пользователя")
    text = models.TextField(null=True, blank=True, verbose_name="Текст заметки")
    created_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заметка контроля"
        verbose_name_plural = "Заметки контроля"

    def __str__(self):
        return self.text[:50] if self.text else "Заметка контроля (без текста)"
