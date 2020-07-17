from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Point, Polygon, Lines
from users import models as user_models

class HomePageView(TemplateView):
	template_name='index.html'

def point_datasets(request):
	points = serialize('geojson', Point.objects.all())
	return HttpResponse(points, content_type='json')

def polygon_datasets(request):
	polygon = serialize('geojson', Polygon.objects.all())
	return HttpResponse(polygon, content_type='json')

def lines_datasets(request):
	lines = serialize('geojson', Lines.objects.all())
	return HttpResponse(lines, content_type='json')

