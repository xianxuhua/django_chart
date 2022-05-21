import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

# 自定义的models需要在setup之后
from djangoProject.models import *
from django.forms.models import model_to_dict
from django.db.models import Q


# select * from gas where 实时浓度 > 100
for i in Gas.objects.filter(实时浓度__gte=100):
    print(model_to_dict(i))


# select * from person where 姓名="男" or 婚姻状况="已婚"
# for i in Person.objects.filter(Q(性别="男") | Q(婚姻状况="已婚")):
#     print(model_to_dict(i))

# select * from person order by 到职日期
# for i in Person.objects.order_by("-到职日期"):
#     print(i.到职日期)
#
# select * from person like 姓名 like '张'
# for i in Person.objects.filter(姓名__contains="张"):
#     print(model_to_dict(i))
#
# for i in Materials.objects.raw("select 1 as id, count(*) as count, 存储方式 from materials group by 存储方式"):
#     print(i.存储方式, i.count)
#
