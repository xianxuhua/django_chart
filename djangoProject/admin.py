# from django.contrib import admin
from django.db.models import Count
from pyecharts.faker import Faker

from .models import *
import xadmin as admin
from django.utils.safestring import mark_safe
from xadmin.views import CommAdminView
from django.shortcuts import render
from pyecharts.charts import Bar, Pie, BMap
from djangoProject import settings


class GlobalSetting:
    site_title = "安全生产管理系统"

    def get_site_menu(self):
        return [
            {
                'title': '图表监控',
                'menus': [
                     {
                         'title': '气体监控',
                         'url': '/admin/gas_view/',
                     },
                    {
                        'title': '风险点监控',
                        'url': '/admin/risk_point_view/',
                    },
                    {
                        'title': '地图',
                        'url': '/admin/map_view/',
                    },
                ]
             },
        ]


class GasView(CommAdminView):
    def get(self, request):
        context = super().get_context()

        gas = Gas.objects.all()
        bar = Bar()
        bar.add_xaxis([i.id for i in gas])
        bar.add_yaxis("实时浓度", [i.实时浓度 for i in gas])

        context["chart"] = mark_safe(bar.render_embed())
        return render(request, 'templates/gas_chart.html', context)


class RiskPointView(CommAdminView):
    def get(self, request):
        context = super().get_context()

        risk_point = RiskPoint.objects.raw("select 1 as id, 风险分级, count(*) as count from risk_point group by 风险分级")
        x = [i.风险分级 for i in risk_point]
        y = [i.count for i in risk_point]
        pie = Pie()
        pie.add("", list(zip(x, y)))
        context["chart"] = mark_safe(pie.render_embed())
        return render(request, 'templates/gas_chart.html', context)


class MapView(CommAdminView):
    def get(self, request):
        context = super().get_context()

        map = BMap()
        map.add_schema(baidu_ak=settings.BAIDU_AK, center=[120.13066322374, 30.240018034923])
        map.add("map", [list(z) for z in zip(Faker.provinces, Faker.values())])

        context["chart"] = mark_safe(map.render_embed())
        return render(request, 'templates/map.html', context)


admin.site.register(CommAdminView, GlobalSetting)
admin.site.register_view("gas_view", GasView, name="gas_view")
admin.site.register_view("risk_point_view", RiskPointView, name="risk_point_view")
admin.site.register_view("map_view", MapView, name="map_view")


class PersonAdmin:
    list_display = ["姓名", "性别", "到职日期", "联系方式", "show_头像", "show_video"]
    list_filter = ["性别", "到职日期"]

    def show_头像(self, obj):
        return mark_safe(f"<img width='100px' height='100px' src='http://127.0.0.1:8000/media/{obj.头像}' />")

    def show_video(self, obj):
        return mark_safe(f'<video width="200" height="150" controls="controls"><source src="http://127.0.0.1:8000/media/{obj.video}" /></video>')


class RiskPointAdmin:
    list_per_page = 10


admin.site.register(Person, PersonAdmin)
admin.site.register(RiskPoint, RiskPointAdmin)
