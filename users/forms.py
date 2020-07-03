from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import (
    shapefile,
    raster
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

class ShapefileForm(forms.ModelForm):
    class Meta:
        model = shapefile
        fields = ('title', 'author', 'region', 'shp')

class RasterForm(forms.ModelForm):
    class Meta:
        model = raster
        fields = ('title', 'author', 'region', 'geotiff')

