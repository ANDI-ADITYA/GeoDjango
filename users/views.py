from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.views.generic import DeleteView
from django.views.generic.edit import UpdateView
from maps.models import (
    Point,
    Administrasi,
    Street
)
from .forms import (
    UserRegisterForm,
    RawPointForm,
    RawAdministrasiForm,
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


# Administrasi-->
# List-->
def AdministrasiListView(request):
    administrasi = Administrasi.objects.all()
    return render(request,'maps/administrasi_list.html',{'administrasi':administrasi})
# Upload-->
def uploadadministrasi(request):
    administrasiform = RawAdministrasiForm()
    if request.method == "POST":
        administrasiform = RawAdministrasiForm(request.POST)
        if administrasiform.is_valid():
            print(administrasiform.cleaned_data)
            Administrasi.objects.create(**administrasiform.cleaned_data)
            return redirect('/')
        else:
            print(administrasiform.errors)
    context = {
            "form": administrasiform
        }
    return render(request,'upload/upload_administrasi.html', context)
# Update Attribute-->
class AdministrasiAttrUpdateView(UpdateView):
    model = Administrasi
    fields = [
        'namobj',
        'remark',
        'lcode',
        'wadmkk',
        'wadmpr',
        'wiadkk',
        'shp_area',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class AdministrasiDeleteView(DeleteView):
    model = Administrasi
    template_name = "maps/administrasi_delete.html"
    success_url = "/administrasi/"


# Street-->
# List-->
def StreetListView(request):
    street = Street.objects.all()
    return render(request,'maps/street_list.html',{'street':street})
# Upload-->
def uploadstreet(request):
    streetform = RawStreetForm()
    if request.method == "POST":
        streetform = RawStreetForm(request.POST)
        if streetform.is_valid():
            print(streetform.cleaned_data)
            Street.objects.create(**streetform.cleaned_data)
            return redirect('/')
        else:
            print(streetform.errors)
    context = {
            "form": streetform
        }
    return render(request,'upload/upload_Street.html', context)
# Update Attribute-->
class StreetAttrUpdateView(UpdateView):
    model = Street
    fields = [
        'namrjl',
        'lcode',
        'spcrjl',
        'starjl',
        'utkrjl',
        'wlyrjl',
        'shp_length',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class StreetDeleteView(DeleteView):
    model = Street
    template_name = "maps/street_delete.html"
    success_url = "/street/"