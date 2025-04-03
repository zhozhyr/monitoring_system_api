from django.core.management.base import BaseCommand
from legacy.models import Tu, Sertificat, ControlNotes, NameTu, TipTu, VidTu, ZavodIzgotovitel
from devices.models import TU, Certificate, ControlNote, NameTU, TypeTU, KindTU, Manufacturer
from opo.models import OPO, HazardClass

def bool_or_none(val):
    return None if val is None else bool(val)

class Command(BaseCommand):
    help = 'Импортирует технические устройства и связанные справочники из MSSQL в PostgreSQL'

    def handle(self, *args, **options):
        # self.import_base_directories()
        # self.import_tu()
        self.import_certificates()
        self.import_control_notes()

    # def import_base_directories(self):
    #     for obj in NameTu.objects.using('mssql').all():
    #         NameTU.objects.update_or_create(id=obj.id, defaults={'name': obj.txt})
    #
    #     for obj in VidTu.objects.using('mssql').all():
    #         KindTU.objects.update_or_create(id=obj.id, defaults={'name': obj.txt})
    #
    #     for obj in TipTu.objects.using('mssql').all():
    #         TypeTU.objects.update_or_create(id=obj.id, defaults={'name': obj.txt})
    #
    #     for obj in ZavodIzgotovitel.objects.using('mssql').all():
    #         Manufacturer.objects.update_or_create(id=obj.id, defaults={'name': obj.txt})
    #
    #     self.stdout.write(self.style.SUCCESS('Справочники импортированы.'))
    #
    # def import_tu(self):
    #     for old in Tu.objects.using('mssql').all():
    #         try:
    #             opo = OPO.objects.get(id=old.id_opo)
    #             name = NameTU.objects.get(id=old.id_naimenovanie_tu)
    #             kind = KindTU.objects.get(id=old.id_vid_tu)
    #             device_type = TypeTU.objects.get(id=old.id_tip_tu) if old.id_tip_tu else None
    #             manufacturer = Manufacturer.objects.get(id=old.id_zavod_izgotovitel) if old.id_zavod_izgotovitel else None
    #             hazard = HazardClass.objects.get(id=old.id_classa_opasnosti) if old.id_classa_opasnosti else None
    #         except Exception as e:
    #             self.stdout.write(self.style.WARNING(f"Пропущен TU {old.id_tu}: {e}"))
    #             continue
    #
    #         TU.objects.update_or_create(
    #             id=old.id_tu,
    #             defaults={
    #                 'registration_number': old.registr_nomer_oborudovaniya_tu,
    #                 'serial_number': old.seriyniy_nomer_tu,
    #                 'state_registration_number': old.gos_registracionniy_nomer,
    #                 'factory_number': old.zavodskoy_nomer,
    #                 'brand': old.marka_tu,
    #                 'technical_characteristics': old.kratkie_tehn_haract_tu,
    #                 'gtt_registration_number': old.registr_nomer_gtt,
    #                 'scheme_number': old.nomer_tu_po_tehn_sheme,
    #                 'manufacture_year': old.god_izgotovleniya,
    #                 'service_life_years': old.norm_srok_ekspluat_let,
    #                 'commissioning_year': old.god_vvoda_v_ekspluat,
    #                 'decommissioning_year': old.god_okonchaniya_ekspluat,
    #                 'wear_percentage': old.procent_iznosa,
    #                 'last_epb_date': old.data_posl_epb,
    #                 'next_epb_date': old.data_sled_epb,
    #                 'last_inspection_date': old.data_ocherednoy_proverki,
    #                 'next_inspection_date': old.data_sled_proverki,
    #                 'permitted_service_life': old.razresh_srok_ekspluat,
    #                 'has_safety_device': bool_or_none(old.nalichie_predohr_ustroystva),
    #                 'safety_device_type': old.tip_predohr_ustr,
    #                 'volume_m3': old.obyom_m3,
    #                 'object_pressure_mpa': old.object_davlenie_mpa,
    #                 'dy_mm': old.dy_mm,
    #                 'type': old.tip,
    #                 'subtype': old.podtip,
    #                 'lifting_capacity_t': old.gruzopodyomnost_t,
    #                 'volume_t': old.obyom_t,
    #                 'equipment_pressure_mpa': old.oborudovanie_davlenie_mpa,
    #                 'modernization_year': old.god_modernizacii,
    #                 'completed_measures': old.provedennie_meropriyatiya,
    #                 'rtn_permission_number': old.nomer_razresheniya_rtn,
    #                 'epb_conclusion_number': old.nomer_zaklyucheniya_epb,
    #                 'passport_present': bool_or_none(old.nalichie_pasporta_tu),
    #                 'opo_info': old.inf_tu_svedeniya_opo,
    #                 'rtn_info': bool_or_none(old.inf_tu_rtn),
    #                 'compliance_certificate_present': bool_or_none(old.nalichie_sertificata_sootvetstviya),
    #                 'rtn_certificate_present': bool_or_none(old.nalichie_sertificata_rtn),
    #                 'manufacturer_id': manufacturer,
    #                 'manufacturer_country': old.strana_proizvoditel,
    #                 'manufacturer_name': old.zavod_izgotovitel_txt,
    #                 'epb_conclusion': old.vivod_epb,
    #                 'total_cycles': old.kol_ciklov,
    #                 'actual_cycles': old.kol_ciklov_fact,
    #                 'replacement_id': old.id_tu_zamen,
    #                 'replacement_number': old.nn_tu_zamen,
    #                 'note1': old.primechanie,
    #                 'note2': old.primechanie2,
    #                 'note3': old.primechanie3,
    #                 'opo_id': opo,
    #                 'hazard_class_id': hazard,
    #                 'device_type_id': device_type,
    #                 'device_name_id': name,
    #                 'kind_device_id': kind,
    #                 'sr_control_presence_id': old.id_nalichie_sr_kontr,
    #                 'cb_oncontrol': bool_or_none(old.cb_oncontrol),
    #                 'date_updated': old.date_upd,
    #                 'updated_by': old.login_upd,
    #                 'is_deleted': bool_or_none(old.isdeleted),
    #             }
    #         )
    #     self.stdout.write(self.style.SUCCESS('Импорт ТУ завершён.'))

    def import_certificates(self):
        for cert in Sertificat.objects.using('mssql').all():
            tu = TU.objects.filter(id=cert.id_tu).first()
            if not tu:
                self.stdout.write(self.style.WARNING(f"Пропущен сертификат {cert.id}: нет TU {cert.id_tu}"))
                continue
            Certificate.objects.update_or_create(
                id=cert.id,
                defaults={
                    'type': cert.tip_sertificata,
                    'number': cert.nomer_sertificata,
                    'date_from': cert.data_sertificata_s,
                    'date_to': cert.data_sertificata_po,
                    'issued_by': cert.kem_vidan,
                    'tu': tu,
                    'scan': cert.scan,
                }
            )
        self.stdout.write(self.style.SUCCESS('Импорт сертификатов завершён.'))

    def import_control_notes(self):
        for note in ControlNotes.objects.using('mssql').all():
            tu = TU.objects.filter(id=note.id_tu).first()
            ControlNote.objects.create(
                tu=tu,
                auto_card_number=note.auto_card,
                text=note.note_txt,
                created_at=note.date_note,
            )
        self.stdout.write(self.style.SUCCESS('Импорт заметок контроля завершён.'))