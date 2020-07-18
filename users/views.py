from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from maps.models import (
    Point,
    Polygon,
    Street
)
from .forms import (
    UserRegisterForm,
    RawPointForm,
    RawPolygonForm,
    RawStreetForm
)

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

##------ POINT -------##
def uploadpoint(request):
    pointform = RawPointForm()
    if request.method == "POST":
        pointform = RawPointForm(request.POST)
        if pointform.is_valid():
            print(pointform.cleaned_data)
            Point.objects.create(**pointform.cleaned_data)
        else:
            print(pointform.errors)
    context = {
            "form": pointform
        }
    return render(request,'upload/upload_Point.html', context)

##------ POLYGON -------##
def uploadpolygon(request):
    polygonform = RawPolygonForm()
    if request.method == "POST":
        polygonform = RawPolygonForm(request.POST)
        if polygonform.is_valid():
            print(polygonform.cleaned_data)
            Polygon.objects.create(**polygonform.cleaned_data)
        else:
            print(polygonform.errors)
    context = {
            "form": polygonform
        }
    return render(request,'upload/upload_Polygon.html', context)

## ------ STREET -------##
def uploadstreet(request):
    pointform = RawStreetForm()
    if request.method == "POST":
        pointform = RawStreetForm(request.POST)
        if pointform.is_valid():
            print(pointform.cleaned_data)
            Street.objects.create(**pointform.cleaned_data)
        else:
            print(pointform.errors)
    context = {
            "form": pointform
        }
    return render(request,'upload/upload_Street.html', context)

