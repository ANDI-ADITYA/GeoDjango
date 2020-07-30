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
    name = forms.CharField()
    category = forms.CharField()
    date = forms.DateField()
    condition = forms. CharField()
    lines = forms.gis.MultiLineStringField (widget=MultiLineStringWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))
    # TODO: Define form fields here


