from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .forms import PointForm, ProvinsiForm
from .models import Point, Provinsi

class ProvinsiCreateView(CreateView):
    model = ProvinsiForm
    template_name = "maps/polygon_create.html"

class HomePageView(TemplateView):
	template_name='index.html'

def point_datasets(request):
	points = serialize('geojson', Point.objects.all())
	return HttpResponse(points, content_type='json')

def provinsi_datasets(request):
	provinsi = serialize('geojson', Provinsi.objects.all())
	return HttpResponse(provinsi, content_type='json')

def create(request):
	point_form = PointForm(request.POST or None)

	if request.method == 'POST':
		if point_form.is_valid():
			point_form.save()

			return redirect('index')

	context = {
		'title':'Create Map Location',
		'point_form':point_form,
	}

	return render(request, 'maps/point_create.html', context)