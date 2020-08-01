from django.contrib import admin
from .models import EduBuild, Administrasi, Street
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class EduBuildAdmin(LeafletGeoAdmin):
	list_display = ('namobj','jnspdk','fgdpdk')

class AdmAdmin(LeafletGeoAdmin):
	list_display = ('namobj','wadmpr','remark',)

class StreetAdmin(LeafletGeoAdmin):
	list_display = ('namrjl','utkrjl','spcrjl')

admin.site.register(EduBuild, EduBuildAdmin)
admin.site.register(Administrasi, AdmAdmin)
admin.site.register(Street, StreetAdmin)