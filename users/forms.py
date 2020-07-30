from django import forms
import floppyforms as forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

##------ USER -------##
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

##------ CUSTOM WIDGET ------##
class PointWidget(forms.gis.PointWidget, forms.gis.BaseOsmWidget):
    map_width = 1000
    map_height = 500
    template_name = 'snippets/osm.html'

    class Media:
        js = (
            'http://openlayers.org/dev/OpenLayers.js',
            'floppyforms/js/MapWidget.js',
        )

class MultiPolygonWidget(forms.gis.MultiPolygonWidget, forms.gis.BaseOsmWidget):
    map_width = 1000
    map_height = 500
    template_name = 'snippets/osm.html'

    class Media:
        js = (
            'http://openlayers.org/dev/OpenLayers.js',
            'floppyforms/js/MapWidget.js',
        )

class MultiLineStringWidget(forms.gis.MultiLineStringWidget, forms.gis.BaseOsmWidget):
    map_width = 1000
    map_height = 500
    template_name = 'snippets/osm.html'

    class Media:
        js = (
            'http://openlayers.org/dev/OpenLayers.js',
            'floppyforms/js/MapWidget.js',
        )

##------ POINT -------##
class RawPointForm(forms.Form):
    name = forms.CharField()
    category = forms.CharField()
    points = forms.gis.PointField(widget=PointWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

##------ ADMINISTRASI -------##
class RawAdministrasiForm(forms.Form):
    namobj = forms.CharField()
    remark = forms.CharField()
    lcode = forms.CharField()
    wadmkk = forms.CharField()
    wadmpr = forms.CharField()
    wiadkk = forms.CharField()
    shp_area = forms.FloatField()
    shp = forms.gis.MultiPolygonField(widget=MultiPolygonWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))

## ------ STREET -------##
class RawStreetForm(forms.Form):
    namrjl = forms.CharField()
    lcode = forms.CharField()
    SPCRJL_CHOICES = (
		('Freeway', 'Freeway'),
		('Highway', 'Highway'),
		('Moderate road', 'Moderate road'),
		('Small road', 'Small road'),
		('Other', 'Other'),
	)
    spcrjl = forms.ChoiceField(choices=SPCRJL_CHOICES)
    STARJL_CHOICES = (
		('Operational', 'Operational'),
		('Will be built', 'Will be built'),
		('Under construction', 'Under construction'),
		('No longer used', 'No longer used'),
		('Other', 'Other'),
	)
    starjl = forms.ChoiceField(choices=STARJL_CHOICES)
    UTKRJL_CHOICES = (
		('Public roads', 'Public roads'),
		('Special roads', 'Special roads'),
		('Other', 'Other'),
	)
    utkrjl = forms. ChoiceField(choices=UTKRJL_CHOICES)
    WLYRJL_CHOICES = (
		('Urban roads', 'Urban roads'),
		('Rural roads', 'Rural roads'),
		('Other', 'Other'),
	)
    wlyrjl = forms. ChoiceField(choices=WLYRJL_CHOICES)
    shp_length = forms.FloatField()
    lines = forms.gis.MultiLineStringField (widget=MultiLineStringWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))
    # TODO: Define form fields here


