from django.contrib import admin
from .models import Point, Administrasi, Street
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class PointAdmin(LeafletGeoAdmin):
	list_display = ('name','category')

class AdmAdmin(LeafletGeoAdmin):
	list_display = ('namobj','wadmpr','remark',)

class StreetAdmin(LeafletGeoAdmin):
	list_display = ('name','category','date')

admin.site.register(Point, PointAdmin)
admin.site.register(Administrasi, AdmAdmin)
admin.site.register(Street, StreetAdmin)