from django.contrib import admin
from .models import Point, Provinsi
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class PointAdmin(LeafletGeoAdmin):
	list_display = ('name','category')
	readonly_fields = [
		'slug',	
	]

class ProvinsiAdmin(LeafletGeoAdmin):
	list_display = ('provinsi','sumber')

admin.site.register(Point, PointAdmin)
admin.site.register(Provinsi, ProvinsiAdmin)