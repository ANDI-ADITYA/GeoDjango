from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Point, Shapefile, Lines
from users import models as user_models

class HomePageView(TemplateView):
	template_name='index.html'

def file_list(request):
	shp = user_models.shapefile.objects.all()
	raster = user_models.raster.objects.all()
	return render(request, 'file.html', {
		'shp': shp,
		'raster': raster
	})

def point_datasets(request):
	points = serialize('geojson', Point.objects.all())
	return HttpResponse(points, content_type='json')

def shapefile_datasets(request):
	shapefile = serialize('geojson', Shapefile.objects.all())
	return HttpResponse(shapefile, content_type='json')

def lines_datasets(request):
	lines = serialize('geojson', Lines.objects.all())
	return HttpResponse(lines, content_type='json')

