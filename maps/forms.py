from django.contrib.gis import forms
from .models import Point, Provinsi

class PointForm(forms.ModelForm):
	class Meta:
		model = Point
		fields = [
			'name',
			'category',
			'points',
		]

class ProvinsiForm(forms.ModelForm):
	class Meta:
		model = Provinsi
		fields = [
			'provinsi',
			'sumber',
			'polygon',
		]