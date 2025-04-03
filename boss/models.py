from django.db import models


class Card(models.Model):
    auto_card = models.IntegerField(db_column='Auto_Card')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                            null=True)  # Field name made lowercase.
    name_i = models.CharField(db_column='Name_i', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                              null=True)  # Field name made lowercase.
    name_o = models.CharField(db_column='Name_o', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                              null=True)  # Field name made lowercase.
    netname = models.CharField(db_column='NetName', max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', max_length=250, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=250, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    fio_d = models.CharField(db_column='FIO_D', max_length=55, db_collation='Cyrillic_General_CI_AS', blank=True,
                             null=True)  # Field name made lowercase.
    full_str = models.CharField(max_length=1000, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Card'


class Pclass(models.Model):
    code_prof = models.IntegerField(db_column='Code_Prof', primary_key=True)  # Field name made lowercase.
    text_prof = models.CharField(db_column='Text_Prof', max_length=100, db_collation='SQL_Latin1_General_CP1251_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PClass'


class People(models.Model):
    pid = models.IntegerField(db_column='pId', primary_key=True)  # Field name made lowercase.
    auto_card = models.IntegerField(db_column='Auto_Card', blank=True, null=True)  # Field name made lowercase.
    in_date = models.DateTimeField(db_column='In_date', blank=True, null=True)  # Field name made lowercase.
    out_date = models.DateTimeField(db_column='Out_date', blank=True, null=True)  # Field name made lowercase.
    struct_code = models.IntegerField(db_column='Struct_Code', blank=True, null=True)  # Field name made lowercase.
    id_firm = models.IntegerField(db_column='id_Firm', blank=True, null=True)  # Field name made lowercase.
    num_tab = models.CharField(db_column='Num_Tab', max_length=8, db_collation='SQL_Latin1_General_CP1251_CI_AS',
                               blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'People'


class PrCurrent(models.Model):
    prid = models.IntegerField(primary_key=True)
    auto_card = models.IntegerField(db_column='Auto_Card', blank=True, null=True)  # Field name made lowercase.
    code_struct_name = models.IntegerField(db_column='Code_Struct_Name', blank=True,
                                           null=True)  # Field name made lowercase.
    code_appoint = models.IntegerField(db_column='Code_Appoint', blank=True, null=True)  # Field name made lowercase.
    w_class = models.IntegerField(db_column='W_Class', blank=True, null=True)  # Field name made lowercase.
    date_trans = models.DateTimeField(db_column='Date_trans', blank=True, null=True)  # Field name made lowercase.
    date_depart = models.DateTimeField(db_column='Date_depart', blank=True, null=True)  # Field name made lowercase.
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pr_Current'


class Rabotniki(models.Model):
    id_rabotnika = models.BigAutoField(db_column='ID_rabotnika', primary_key=True)  # Field name made lowercase.
    familiya = models.CharField(db_column='Familiya', max_length=200,
                                db_collation='SQL_Latin1_General_CP1251_CI_AS')  # Field name made lowercase.
    imya = models.CharField(db_column='Imya', max_length=200,
                            db_collation='SQL_Latin1_General_CP1251_CI_AS')  # Field name made lowercase.
    otchestvo = models.CharField(db_column='Otchestvo', max_length=200, db_collation='SQL_Latin1_General_CP1251_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200,
                             db_collation='SQL_Latin1_General_CP1251_CI_AS')  # Field name made lowercase.
    id_strukturn_podrazd = models.BigIntegerField(db_column='ID_strukturn_podrazd')  # Field name made lowercase.
    id_doljnosti = models.BigIntegerField(db_column='ID_doljnosti')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rabotniki'


class ResponsibleWorkers(models.Model):
    auto_card = models.IntegerField(db_column='Auto_Card', blank=True, null=True)  # Field name made lowercase.
    id_struct = models.IntegerField(db_column='id_Struct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responsible_Workers'


class Setup(models.Model):
    id_firm = models.IntegerField(db_column='Id_Firm', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, db_collation='SQL_Latin1_General_CP1251_CI_AS',
                            blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='Short_name', max_length=100,
                                  db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                  null=True)  # Field name made lowercase.
    id_struct_parent = models.IntegerField(db_column='Id_struct_parent', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup'


class Structs(models.Model):
    struct_code = models.IntegerField(db_column='Struct_Code', primary_key=True)  # Field name made lowercase.
    struct_name = models.CharField(db_column='Struct_Name', max_length=255,
                                   db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                   null=True)  # Field name made lowercase.
    struct_parent = models.IntegerField(db_column='Struct_Parent', blank=True, null=True)  # Field name made lowercase.
    id_firm = models.IntegerField(db_column='id_Firm', blank=True, null=True)  # Field name made lowercase.
    no_print = models.SmallIntegerField(blank=True, null=True)
    struct_lev = models.SmallIntegerField(db_column='Struct_Lev', blank=True, null=True)  # Field name made lowercase.
    struct_root = models.IntegerField(db_column='Struct_root', blank=True, null=True)  # Field name made lowercase.
    struct_name_r = models.CharField(db_column='struct_name_R', max_length=255,
                                     db_collation='SQL_Latin1_General_CP1251_CI_AS', blank=True,
                                     null=True)  # Field name made lowercase.
    hist_parent = models.IntegerField(db_column='Hist_Parent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Structs'


class Tree(models.Model):
    id_tree = models.IntegerField(primary_key=True)
    struct_parent = models.IntegerField(db_column='Struct_Parent', blank=True, null=True)  # Field name made lowercase.
    struct_code = models.IntegerField(db_column='Struct_Code', blank=True, null=True)  # Field name made lowercase.
    lev = models.SmallIntegerField(blank=True, null=True)
    id_firm = models.IntegerField(blank=True, null=True)
    rep_branch_num = models.IntegerField(db_column='REP_BRANCH_NUM', blank=True,
                                         null=True)  # Field name made lowercase.
    rep_branch_id = models.IntegerField(db_column='REP_BRANCH_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tree'


class PrtbOpStructs(models.Model):
    id_op_structs = models.CharField(primary_key=True, max_length=36)
    id_firm = models.IntegerField(blank=True, null=True)
    struct_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prtb_op_structs'
