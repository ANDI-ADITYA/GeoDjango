from django import forms
import floppyforms as forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

class MultiPolygonWidget(forms.gis.MultiPolygonWidget, forms.gis.BaseOsmWidget):
    map_width = 1000
    map_height = 500
    template_name = 'snippets/osm.html'

    class Media:
        js = (
            'http://openlayers.org/dev/OpenLayers.js',
            'floppyforms/js/MapWidget.js',
        )

class RawPolygonForm(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    region = forms. CharField()
    shp = forms.gis.MultiPolygonField(widget=MultiPolygonWidget(attrs={
        'id': 'gis',
        'style': 'width: 100%;'
    }))
    # TODO: Define form fields here


