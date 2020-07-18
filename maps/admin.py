from django.contrib import admin
from .models import Point, Polygon, Street
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class PointAdmin(LeafletGeoAdmin):
	list_display = ('name','category')

class PolyAdmin(LeafletGeoAdmin):
	list_display = ('title','author','region')

class StreetAdmin(LeafletGeoAdmin):
	list_display = ('name','category','date')

admin.site.register(Point, PointAdmin)
admin.site.register(Polygon, PolyAdmin)
admin.site.register(Street, StreetAdmin)