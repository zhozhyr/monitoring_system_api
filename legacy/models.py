from django.db import models


#
# class ClassOpasnosti(models.Model):
#     id = models.IntegerField(primary_key=True)
#     txt = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)
#
#     class Meta:
#         app_label = 'legacy'
#         managed = False
#         db_table = 'Class_opasnosti'
#
#
# class Opo(models.Model):
#     id_opo = models.BigAutoField(db_column='ID_OPO', primary_key=True)  # Field name made lowercase.
#     id_type_opo = models.BigIntegerField(db_column='ID_type_OPO')  # Field name made lowercase.
#     id_strukturn_podrazd = models.BigIntegerField(db_column='ID_strukturn_podrazd')  # Field name made lowercase.
#     txt = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)
#     txt_short = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)
#     reg_number = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)
#
#     class Meta:
#         app_label = 'legacy'
#         managed = False
#         db_table = 'OPO'
#
#
# class TipOpo(models.Model):
#     id = models.IntegerField(primary_key=True)
#     txt = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)
#     txt_short = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)
#     reg_number = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)
#
#     class Meta:
#         app_label = 'legacy'
#         managed = False
#         db_table = 'Tip_OPO'

class ControlNotes(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tu = models.IntegerField(db_column='id_TU', blank=True, null=True)  # Field name made lowercase.
    auto_card = models.IntegerField(db_column='Auto_Card', blank=True, null=True)  # Field name made lowercase.
    note_txt = models.CharField(max_length=5000, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)
    date_note = models.DateTimeField(db_column='Date_Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'legacy'
        db_table = 'Control_Notes'


class Nalichie(models.Model):
    id = models.IntegerField(primary_key=True)
    txt = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'legacy'
        db_table = 'Nalichie'


class NalichiePasportaTu(models.Model):
    id = models.IntegerField(primary_key=True)
    txt = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'legacy'
        db_table = 'Nalichie_pasporta_TU'


class NameTu(models.Model):
    id = models.IntegerField(primary_key=True)
    txt = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'legacy'
        db_table = 'Name_TU'


class Sertificat(models.Model):
    id = models.IntegerField(db_column='ID_sertificata', primary_key=True)  # Field name made lowercase.
    tip_sertificata = models.CharField(db_column='Tip_sertificata', max_length=500,
                                       db_collation='SQL_Latin1_General_CP1251_CI_AS')  # Field name made lowercase.
    nomer_sertificata = models.CharField(db_column='Nomer_sertificata', max_length=200,
                                         db_collation='SQL_Latin1_General_CP1251_CI_AS')  # Field name made lowercase.
    data_sertificata_s = models.DateField(db_column='Data_sertificata_s', blank=True,
                                          null=True)  # Field name made lowercase.
    data_sertificata_po = models.DateField(db_column='Data_sertificata_po', blank=True,
                                           null=True)  # Field name made lowercase.
    kem_vidan = models.CharField(db_column='Kem_vidan', max_length=500,
                                 db_collation='SQL_Latin1_General_CP1251_CI_AS')  # Field name made lowercase.
    id_tu = models.BigIntegerField(db_column='ID_TU')  # Field name made lowercase.
    scan = models.BinaryField(db_column='Scan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'legacy'
        db_table = 'Sertificat'


class Tu(models.Model):
    registr_nomer_oborudovaniya_tu = models.CharField(db_column='Registr_nomer_oborudovaniya_TU', max_length=200,
                                                      db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                                      null=True)  # Field name made lowercase.
    seriyniy_nomer_tu = models.CharField(db_column='Seriyniy_nomer_TU', max_length=200,
                                         db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                         null=True)  # Field name made lowercase.
    gos_registracionniy_nomer = models.CharField(db_column='Gos_registracionniy_nomer', max_length=200,
                                                 db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                                 null=True)  # Field name made lowercase.
    zavodskoy_nomer = models.CharField(db_column='Zavodskoy_nomer', max_length=200,
                                       db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                       null=True)  # Field name made lowercase.
    marka_tu = models.CharField(db_column='Marka_TU', max_length=500, db_collation='SQL_Latin1_General_CP1251_CI_AS',
                                blank=True, null=True)  # Field name made lowercase.
    kratkie_tehn_haract_tu = models.CharField(db_column='Kratkie_tehn_haract_TU', max_length=200,
                                              db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                              null=True)  # Field name made lowercase.
    registr_nomer_gtt = models.CharField(db_column='Registr_nomer_GTT', max_length=200,
                                         db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                         null=True)  # Field name made lowercase.
    nomer_tu_po_tehn_sheme = models.CharField(db_column='Nomer_TU_po_tehn_sheme', max_length=200,
                                              db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                              null=True)  # Field name made lowercase.
    god_izgotovleniya = models.CharField(db_column='God_izgotovleniya', max_length=200,
                                         db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                         null=True)  # Field name made lowercase.
    norm_srok_ekspluat_let = models.SmallIntegerField(db_column='Norm_srok_ekspluat_let', blank=True,
                                                      null=True)  # Field name made lowercase.
    god_vvoda_v_ekspluat = models.SmallIntegerField(db_column='God_vvoda_v_ekspluat', blank=True,
                                                    null=True)  # Field name made lowercase.
    god_okonchaniya_ekspluat = models.SmallIntegerField(db_column='God_okonchaniya_ekspluat', blank=True,
                                                        null=True)  # Field name made lowercase.
    procent_iznosa = models.FloatField(db_column='Procent_iznosa', blank=True, null=True)  # Field name made lowercase.
    data_posl_epb = models.DateField(db_column='Data_posl_EPB', blank=True, null=True)  # Field name made lowercase.
    data_sled_epb = models.DateField(db_column='Data_sled_EPB', blank=True, null=True)  # Field name made lowercase.
    data_ocherednoy_proverki = models.DateField(db_column='Data_ocherednoy_proverki', blank=True,
                                                null=True)  # Field name made lowercase.
    data_sled_proverki = models.DateField(db_column='Data_sled_proverki', blank=True,
                                          null=True)  # Field name made lowercase.
    razresh_srok_ekspluat = models.SmallIntegerField(db_column='Razresh_srok_ekspluat', blank=True,
                                                     null=True)  # Field name made lowercase.
    nalichie_predohr_ustroystva = models.IntegerField(db_column='Nalichie_predohr_ustroystva', blank=True,
                                                      null=True)  # Field name made lowercase.
    tip_predohr_ustr = models.CharField(db_column='Tip_predohr_ustr', max_length=200,
                                        db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                        null=True)  # Field name made lowercase.
    obyom_m3 = models.FloatField(db_column='Obyom_m3', blank=True, null=True)  # Field name made lowercase.
    object_davlenie_mpa = models.FloatField(db_column='Object_davlenie_MPa', blank=True,
                                            null=True)  # Field name made lowercase.
    dy_mm = models.FloatField(db_column='Dy_mm', blank=True, null=True)  # Field name made lowercase.
    tip = models.CharField(db_column='Tip', max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                           null=True)  # Field name made lowercase.
    podtip = models.CharField(db_column='Podtip', max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS',
                              blank=True, null=True)  # Field name made lowercase.
    gruzopodyomnost_t = models.FloatField(db_column='Gruzopodyomnost_t', blank=True,
                                          null=True)  # Field name made lowercase.
    obyom_t = models.FloatField(db_column='Obyom_t', blank=True, null=True)  # Field name made lowercase.
    oborudovanie_davlenie_mpa = models.FloatField(db_column='Oborudovanie_davlenie_MPa', blank=True,
                                                  null=True)  # Field name made lowercase.
    god_modernizacii = models.SmallIntegerField(db_column='God_modernizacii', blank=True,
                                                null=True)  # Field name made lowercase.
    provedennie_meropriyatiya = models.CharField(db_column='Provedennie_meropriyatiya', max_length=200,
                                                 db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                                 null=True)  # Field name made lowercase.
    nomer_razresheniya_rtn = models.CharField(db_column='Nomer_razresheniya_RTN', max_length=200,
                                              db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                              null=True)  # Field name made lowercase.
    nomer_zaklyucheniya_epb = models.CharField(db_column='Nomer_zaklyucheniya_EPB', max_length=200,
                                               db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                               null=True)  # Field name made lowercase.
    nalichie_pasporta_tu = models.IntegerField(db_column='Nalichie_pasporta_TU', blank=True,
                                               null=True)  # Field name made lowercase.
    inf_tu_svedeniya_opo = models.CharField(db_column='Inf_TU_svedeniya_OPO', max_length=200,
                                            db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                            null=True)  # Field name made lowercase.
    inf_tu_rtn = models.CharField(db_column='Inf_TU_RTN', max_length=200,
                                  db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                  null=True)  # Field name made lowercase.
    nalichie_sertificata_sootvetstviya = models.IntegerField(db_column='Nalichie_sertificata_sootvetstviya', blank=True,
                                                             null=True)  # Field name made lowercase.
    nalichie_sertificata_rtn = models.IntegerField(db_column='Nalichie_sertificata_RTN', blank=True,
                                                   null=True)  # Field name made lowercase.
    primechanie = models.TextField(db_column='Primechanie', db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                   null=True)  # Field name made lowercase.
    id_opo = models.BigIntegerField(db_column='ID_OPO')  # Field name made lowercase.
    id_classa_opasnosti = models.BigIntegerField(db_column='ID_classa_opasnosti', blank=True,
                                                 null=True)  # Field name made lowercase.
    id_zavod_izgotovitel = models.BigIntegerField(db_column='ID_zavod_izgotovitel', blank=True,
                                                  null=True)  # Field name made lowercase.
    id_vid_tu = models.BigIntegerField(db_column='ID_vid_TU')  # Field name made lowercase.
    id_tip_tu = models.BigIntegerField(db_column='ID_tip_TU', blank=True, null=True)  # Field name made lowercase.
    id_naimenovanie_tu = models.BigIntegerField(db_column='ID_naimenovanie_TU')  # Field name made lowercase.
    id_tu = models.IntegerField(db_column='ID_TU', primary_key=True)  # Field name made lowercase.
    id_rtn = models.IntegerField(db_column='id_RTN', blank=True, null=True)  # Field name made lowercase.
    strana_proizvoditel = models.CharField(db_column='Strana_proizvoditel', max_length=200,
                                           db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                           null=True)  # Field name made lowercase.
    vivod_epb = models.CharField(db_column='Vivod_EPB', max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.
    kol_ciklov = models.IntegerField(db_column='Kol_ciklov', blank=True, null=True)  # Field name made lowercase.
    kol_ciklov_fact = models.IntegerField(db_column='Kol_ciklov_fact', blank=True,
                                          null=True)  # Field name made lowercase.
    id_nalichie_sr_kontr = models.IntegerField(blank=True, null=True)
    id_tu_zamen = models.IntegerField(db_column='id_TU_Zamen', blank=True, null=True)  # Field name made lowercase.
    nn_tu_zamen = models.CharField(db_column='NN_TU_Zamen', max_length=200,
                                   db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                   null=True)  # Field name made lowercase.
    id_vid_tu_j = models.IntegerField(db_column='id_Vid_TU_j', blank=True, null=True)  # Field name made lowercase.
    id_tip_tu_j = models.IntegerField(db_column='id_Tip_TU_j', blank=True, null=True)  # Field name made lowercase.
    cb_oncontrol = models.IntegerField(db_column='cb_onControl', blank=True, null=True)  # Field name made lowercase.
    primechanie2 = models.TextField(db_column='Primechanie2', db_collation='SQL_Latin1_General_CP1251_CI_AS',
                                    blank=True, null=True)  # Field name made lowercase.
    primechanie3 = models.TextField(db_column='Primechanie3', db_collation='SQL_Latin1_General_CP1251_CI_AS',
                                    blank=True, null=True)  # Field name made lowercase.
    zavod_izgotovitel_txt = models.CharField(db_column='Zavod_Izgotovitel_txt', max_length=500,
                                             db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                             null=True)  # Field name made lowercase.
    date_upd = models.DateTimeField(db_column='Date_upd', blank=True, null=True)  # Field name made lowercase.
    login_upd = models.CharField(db_column='Login_upd', max_length=100, db_collation='SQL_Latin1_General_CP1251_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'legacy'
        managed = False
        db_table = 'TU'


class TuRtn(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    txt = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TU_RTN'
        app_label = 'legacy'


class TipTu(models.Model):
    id = models.IntegerField(primary_key=True)
    txt = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tip_TU'
        app_label = 'legacy'


# class TipTuJ(models.Model):
#     id = models.IntegerField(blank=True, primary_key=True)
#     txt = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'Tip_TU_j'
#         app_label = 'legacy'


class VidTu(models.Model):
    id = models.IntegerField(primary_key=True)
    txt = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vid_TU'
        app_label = 'legacy'


# class VidTuJ(models.Model):
#     id = models.IntegerField(blank=True, null=True, primary_key=True)
#     txt = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'Vid_TU_j'
#         app_label = 'legacy'


class ZavodIzgotovitel(models.Model):
    id = models.IntegerField(primary_key=True)
    txt = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Zavod_izgotovitel'
        app_label = 'legacy'
