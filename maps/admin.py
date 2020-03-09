from django.contrib import admin
from .models import Point, shapefile
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class PointAdmin(LeafletGeoAdmin):
	list_display = ('name','category')
	readonly_fields = [
		'slug',	
	]

class ShapeAdmin(LeafletGeoAdmin):
	list_display = ('title', 'author')

admin.site.register(Point, PointAdmin)
admin.site.register(shapefile, ShapeAdmin)