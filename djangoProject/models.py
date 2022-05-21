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
    名称 = models.CharField(max_length=255, blank=True, null=True)
    编码 = models.CharField(max_length=255, blank=True, null=True)
    危险源级别 = models.CharField(max_length=255, blank=True, null=True)
    r值 = models.FloatField(db_column='R值', blank=True, null=True)  # Field name made lowercase.
    厂区人数 = models.IntegerField(blank=True, null=True)
    主要危险性 = models.CharField(max_length=255, blank=True, null=True)

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
    物资类别 = models.CharField(max_length=255, blank=True, null=True)
    名称 = models.CharField(max_length=255, blank=True, null=True)
    型号 = models.CharField(max_length=255, blank=True, null=True)
    数量 = models.IntegerField(blank=True, null=True)
    功能用途 = models.CharField(max_length=255, blank=True, null=True)
    自储数量 = models.IntegerField(blank=True, null=True)
    代储数量 = models.IntegerField(blank=True, null=True)
    储存单位 = models.CharField(max_length=255, blank=True, null=True)
    储存地址 = models.CharField(max_length=255, blank=True, null=True)
    联系人 = models.CharField(max_length=255, blank=True, null=True)
    联系电话 = models.CharField(max_length=11, blank=True, null=True)
    备注 = models.CharField(max_length=255, blank=True, null=True)
    经度 = models.FloatField(blank=True, null=True)
    纬度 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_supplies'


class Gas(models.Model):
    所属罐区 = models.ForeignKey('TankFarm', models.DO_NOTHING, db_column='所属罐区', blank=True, null=True)
    是否报警 = models.IntegerField(blank=True, null=True)
    实时浓度 = models.IntegerField(blank=True, null=True)
    采集时间 = models.DateTimeField(blank=True, null=True)
    气体类型 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gas'


class Materials(models.Model):
    物料名称 = models.CharField(max_length=255, blank=True, null=True)
    年用量_t_field = models.FloatField(db_column='年用量（t）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    最大储量_t_field = models.FloatField(db_column='最大储量（t）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cas号 = models.CharField(db_column='CAS号', max_length=255, blank=True, null=True)  # Field name made lowercase.
    存储方式 = models.CharField(max_length=255, blank=True, null=True)
    主要危险性 = models.CharField(max_length=255, blank=True, null=True)
    备注 = models.CharField(max_length=255, blank=True, null=True)
    物料类别 = models.CharField(max_length=255, blank=True, null=True)
    状态 = models.CharField(max_length=255, blank=True, null=True)
    是否领证 = models.IntegerField(blank=True, null=True)
    重点监管 = models.IntegerField(blank=True, null=True)
    剧毒 = models.IntegerField(blank=True, null=True)
    易制毒 = models.IntegerField(blank=True, null=True)
    易制爆 = models.IntegerField(blank=True, null=True)
    标识 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materials'


class Person(models.Model):
    工号 = models.CharField(max_length=255, blank=True, null=True)
    姓名 = models.CharField(max_length=255, blank=True, null=True)
    性别 = models.CharField(max_length=255, blank=True, null=True, choices=[
        ["男", "男"],
        ["女", "女"],
    ])
    身份证号 = models.CharField(max_length=255, blank=True, null=True)
    人员类别 = models.CharField(max_length=255, blank=True, null=True)
    出生日期 = models.DateTimeField(blank=True, null=True)
    到职日期 = models.DateField(blank=True, null=True)
    婚姻状况 = models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    职位 = models.CharField(max_length=255, blank=True, null=True)
    学历 = models.CharField(max_length=255, blank=True, null=True)
    贯籍 = models.CharField(max_length=255, blank=True, null=True)
    民族 = models.CharField(max_length=255, blank=True, null=True)
    专业 = models.CharField(max_length=255, blank=True, null=True)
    联系方式 = models.CharField(max_length=11, blank=True, null=True)
    责任区域 = models.CharField(max_length=255, blank=True, null=True)
    头像 = models.ImageField(upload_to="head_img", blank=True, null=True)
    video = models.FileField(upload_to="video", blank=True, null=True)

    class Meta:
        verbose_name = "人员管理"
        verbose_name_plural = verbose_name
        managed = False
        db_table = 'person'


class RiskPoint(models.Model):
    风险点名称 = models.CharField(max_length=255, blank=True, null=True)
    风险类别 = models.CharField(max_length=255, blank=True, null=True)
    事故类型 = models.CharField(max_length=255, blank=True, null=True)
    风险分级 = models.CharField(max_length=255, blank=True, null=True)
    状态 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'risk_point'


class StorageTank(models.Model):
    储罐名称 = models.CharField(max_length=255, blank=True, null=True)
    储罐类型 = models.CharField(max_length=255, blank=True, null=True)
    容积 = models.FloatField(blank=True, null=True)
    材质 = models.CharField(max_length=255, blank=True, null=True)
    火灾危险性等级 = models.CharField(max_length=255, blank=True, null=True)
    储存物料名称 = models.CharField(max_length=255, blank=True, null=True)
    cas号 = models.CharField(max_length=255, blank=True, null=True)
    位号 = models.CharField(max_length=255, blank=True, null=True)
    罐径 = models.FloatField(blank=True, null=True)
    罐高 = models.FloatField(blank=True, null=True)
    储罐区面积 = models.FloatField(blank=True, null=True)
    有无防火堤 = models.IntegerField(blank=True, null=True)
    防火堤所围面积 = models.FloatField(blank=True, null=True)
    危化品类别 = models.CharField(max_length=255, blank=True, null=True)
    所属储罐区 = models.ForeignKey('TankFarm', models.DO_NOTHING, db_column='所属储罐区', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_tank'


class TankFarm(models.Model):
    储罐区编号 = models.CharField(max_length=255, blank=True, null=True)
    储罐区名称 = models.CharField(max_length=255, blank=True, null=True)
    储罐区面积_field = models.FloatField(db_column='储罐区面积(㎡)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    储罐个数 = models.IntegerField(blank=True, null=True)
    经度 = models.FloatField(blank=True, null=True)
    纬度 = models.FloatField(blank=True, null=True)
    罐间最小距离 = models.FloatField(blank=True, null=True)
    备注 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tank_farm'
