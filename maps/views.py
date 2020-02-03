from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Point, Provinsi

class HomePageView(TemplateView):
	template_name='index.html'

def point_datasets(request):
	points = serialize('geojson', Point.objects.all())
	return HttpResponse(points, content_type='json')

def provinsi_datasets(request):
	provinsi = serialize('geojson', Provinsi.objects.all())
	return HttpResponse(provinsi, content_type='json')
