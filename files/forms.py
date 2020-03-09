from django import forms
from maps.models import shapefile

class ShapefileForm(forms.ModelForm):
    class Meta:
        model = shapefile
        fields = ('title', 'author', 'shp')