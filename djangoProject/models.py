# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BigRisk(models.Model):
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ??????????????? = models.CharField(max_length=255, blank=True, null=True)
    r??? = models.FloatField(db_column='R???', blank=True, null=True)  # Field name made lowercase.
    ???????????? = models.IntegerField(blank=True, null=True)
    ??????????????? = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'big_risk'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmergencySupplies(models.Model):
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.IntegerField(blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.IntegerField(blank=True, null=True)
    ???????????? = models.IntegerField(blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ????????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.CharField(max_length=11, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.FloatField(blank=True, null=True)
    ?????? = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_supplies'


class Gas(models.Model):
    ???????????? = models.ForeignKey('TankFarm', models.DO_NOTHING, db_column='????????????', blank=True, null=True)
    ???????????? = models.IntegerField(blank=True, null=True)
    ???????????? = models.IntegerField(blank=True, null=True)
    ???????????? = models.DateTimeField(blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gas'


class Materials(models.Model):
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ?????????_t_field = models.FloatField(db_column='????????????t???', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ????????????_t_field = models.FloatField(db_column='???????????????t???', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cas??? = models.CharField(db_column='CAS???', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ??????????????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.IntegerField(blank=True, null=True)
    ???????????? = models.IntegerField(blank=True, null=True)
    ?????? = models.IntegerField(blank=True, null=True)
    ????????? = models.IntegerField(blank=True, null=True)
    ????????? = models.IntegerField(blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materials'


class Person(models.Model):
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True, choices=[
        ["???", "???"],
        ["???", "???"],
    ])
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.DateTimeField(blank=True, null=True)
    ???????????? = models.DateField(blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.CharField(max_length=11, blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.ImageField(upload_to="head_img", blank=True, null=True)
    video = models.FileField(upload_to="video", blank=True, null=True)

    class Meta:
        verbose_name = "????????????"
        verbose_name_plural = verbose_name
        managed = False
        db_table = 'person'


class RiskPoint(models.Model):
    ??????????????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'risk_point'


class StorageTank(models.Model):
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.FloatField(blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ????????????????????? = models.CharField(max_length=255, blank=True, null=True)
    ?????????????????? = models.CharField(max_length=255, blank=True, null=True)
    cas??? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)
    ?????? = models.FloatField(blank=True, null=True)
    ?????? = models.FloatField(blank=True, null=True)
    ??????????????? = models.FloatField(blank=True, null=True)
    ??????????????? = models.IntegerField(blank=True, null=True)
    ????????????????????? = models.FloatField(blank=True, null=True)
    ??????????????? = models.CharField(max_length=255, blank=True, null=True)
    ??????????????? = models.ForeignKey('TankFarm', models.DO_NOTHING, db_column='???????????????', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_tank'


class TankFarm(models.Model):
    ??????????????? = models.CharField(max_length=255, blank=True, null=True)
    ??????????????? = models.CharField(max_length=255, blank=True, null=True)
    ???????????????_field = models.FloatField(db_column='???????????????(???)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ???????????? = models.IntegerField(blank=True, null=True)
    ?????? = models.FloatField(blank=True, null=True)
    ?????? = models.FloatField(blank=True, null=True)
    ?????????????????? = models.FloatField(blank=True, null=True)
    ?????? = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tank_farm'
