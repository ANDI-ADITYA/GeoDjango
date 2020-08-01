from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import EduBuild, Administrasi, Street
from users import models as user_models

class HomePageView(TemplateView):
	template_name='home/index.html'

def edubuild_datasets(request):
	edubuild = serialize('geojson', EduBuild.objects.all())
	return HttpResponse(edubuild, content_type='json')

def administrasi_datasets(request):
	administrasi = serialize('geojson', Administrasi.objects.all())
	return HttpResponse(administrasi, content_type='json')

def street_datasets(request):
	street = serialize('geojson', Street.objects.all())
	return HttpResponse(street, content_type='json')

