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

##------ Education Building -------##
class RawEduBuildForm(forms.Form):
    namobj = forms.CharField()
    remark = forms.CharField()
    lcode = forms.CharField()
    FGDPDK_CHOICES = (
        ('College', 'College'),
        ('Senior secondary Education (SMA, MA, SMALB)', 'Senior secondary Education (SMA, MA, SMALB)'),
		('Vocational secondary education (SMK, MAK)', 'Vocational secondary education (SMK, MAK)'),
		('First secondary education (SMP, MTs, SMPLB)', 'First secondary education (SMP, MTs, SMPLB)'),
		('Primary education (SD, MI, SDLB)', 'Primary education (SD, MI, SDLB)'),
		('Early childhood Education (TK, RA, TPA, KB)', 'Early childhood Education (TK, RA, TPA, KB)'),
		('Course Board', 'Course Board'),
		('Training Institute', 'Training Institute'),
		('Community Learning Activities Center', 'Community Learning Activities Center'),
		('Religious Education (Pesantren, Pasraman, etc.)', 'Religious Education (Pesantren, Pasraman, etc.)'),
		('Other', 'Other'),
    )
    fgdpdk = forms.ChoiceField(choices=FGDPDK_CHOICES)
    JNSPDK_CHOICES = (
        ('General education', 'General education'),
		('Vocational education', 'Vocational education'),
		('Academic education', 'Academic education'),
		('Professional education', 'Professional education'),
		('Religious education', 'Religious education'),
		('Special education', 'Special education'),
		('Special Service Education', 'Special Service Education'),
		('Other', 'Other'),
    )
    jnspdk = forms.ChoiceField(choices=JNSPDK_CHOICES)
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


