from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.views.generic import DeleteView
from django.views.generic.edit import UpdateView
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

# Register-->
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


# Point-->
# List-->
def PointListView(request):
    point = Point.objects.all()
    return render(request,'maps/point_list.html',{'point':point})
# Upload-->
def uploadpoint(request):
    pointform = RawPointForm()
    if request.method == "POST":
        pointform = RawPointForm(request.POST)
        if pointform.is_valid():
            print(pointform.cleaned_data)
            Point.objects.create(**pointform.cleaned_data)
            return redirect('/')
        else:
            print(pointform.errors)
    context = {
            "form": pointform
        }
    return render(request,'upload/upload_Point.html', context)
# Update Attribute-->
class PointAttrUpdateView(UpdateView):
    model = Point
    fields = [
        'name',
        'category',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class PointDeleteView(DeleteView):
    model = Point
    template_name = "maps/point_delete.html"
    success_url = "/point/"


# Polygon-->
# List-->
def PolygonListView(request):
    polygon = Polygon.objects.all()
    return render(request,'maps/polygon_list.html',{'polygon':polygon})
# Upload-->
def uploadpolygon(request):
    polygonform = RawPolygonForm()
    if request.method == "POST":
        polygonform = RawPolygonForm(request.POST)
        if polygonform.is_valid():
            print(polygonform.cleaned_data)
            Polygon.objects.create(**polygonform.cleaned_data)
            return redirect('/')
        else:
            print(polygonform.errors)
    context = {
            "form": polygonform
        }
    return render(request,'upload/upload_Polygon.html', context)
# Update Attribute-->
class PolygonAttrUpdateView(UpdateView):
    model = Polygon
    fields = [
        'title',
        'author',
        'region',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class PolygonDeleteView(DeleteView):
    model = Polygon
    template_name = "maps/polygon_delete.html"
    success_url = "/polygon/"


# Street-->
# List-->
def StreetListView(request):
    street = Street.objects.all()
    return render(request,'maps/street_list.html',{'street':street})
# Upload-->
def uploadstreet(request):
    pointform = RawStreetForm()
    if request.method == "POST":
        pointform = RawStreetForm(request.POST)
        if pointform.is_valid():
            print(pointform.cleaned_data)
            Street.objects.create(**pointform.cleaned_data)
            return redirect('/')
        else:
            print(pointform.errors)
    context = {
            "form": pointform
        }
    return render(request,'upload/upload_Street.html', context)
# Update Attribute-->
class StreetAttrUpdateView(UpdateView):
    model = Street
    fields = [
        'name',
        'category',
        'date',
        'condition',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class StreetDeleteView(DeleteView):
    model = Street
    template_name = "maps/street_delete.html"
    success_url = "/street/"