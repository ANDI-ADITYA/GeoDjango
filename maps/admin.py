from django.contrib import admin
from .models import Point, Polygon, Lines
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class PointAdmin(LeafletGeoAdmin):
	list_display = ('name','category')

class PolyAdmin(LeafletGeoAdmin):
	list_display = ('title','author', 'region')

class LineAdmin(LeafletGeoAdmin):
	list_display = ('name','category')

admin.site.register(Point, PointAdmin)
admin.site.register(Polygon, PolyAdmin)
admin.site.register(Lines, LineAdmin)