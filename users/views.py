from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.views.generic import DeleteView
from django.views.generic.edit import UpdateView
from maps.models import (
    EduBuild,
    Administrasi,
    Street
)
from .forms import (
    UserRegisterForm,
    RawEduBuildForm,
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


# Education Building-->
# List-->
def EduBuildListView(request):
    edubuild = EduBuild.objects.all()
    return render(request,'maps/edubuild_list.html',{'edubuild':edubuild})
# Upload-->
def uploadedubuild(request):
    edubuildform = RawEduBuildForm()
    if request.method == "POST":
        edubuildform = RawEduBuildForm(request.POST)
        if edubuildform.is_valid():
            print(edubuildform.cleaned_data)
            EduBuild.objects.create(**edubuildform.cleaned_data)
            return redirect('/')
        else:
            print(edubuildform.errors)
    context = {
            "form": edubuildform
        }
    return render(request,'upload/upload_edubuild.html', context)
# Update Attribute-->
class EduBuildAttrUpdateView(UpdateView):
    model = EduBuild
    fields = [
        'namobj',
        'remark',
        'lcode',
        'fgdpdk',
        'jnspdk',
    ]
    template_name_suffix = '_update_form'
    success_url = '/'
# Delete-->
class EduBuildDeleteView(DeleteView):
    model = EduBuild
    template_name = "maps/edubuild_delete.html"
    success_url = "/street/"


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