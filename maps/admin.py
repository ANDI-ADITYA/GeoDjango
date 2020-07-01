from django.contrib import admin
from .models import Point, Shapefile, Lines
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class PointAdmin(LeafletGeoAdmin):
	list_display = ('name','category')

class ShapeAdmin(LeafletGeoAdmin):
	list_display = ('objname', 'wadmkk')

class LineAdmin(LeafletGeoAdmin):
	list_display = ('name','category')

admin.site.register(Point, PointAdmin)
admin.site.register(Shapefile, ShapeAdmin)
admin.site.register(Lines, LineAdmin)