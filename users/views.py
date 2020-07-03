from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .forms import (
    UserRegisterForm,
    ShapefileForm,
    RasterForm
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

def uploadshapefile(request):
    if request.method == 'POST':
        form = ShapefileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files')
    else:
        form = ShapefileForm()
    return render(request,'upload_Shapefile.html', {
        'form': form
    })

def uploadraster(request):
    if request.method == 'POST':
        form = RasterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files')
    else:
        form = RasterForm()
    return render(request,'upload_Raster.html', {
        'form': form
    })

