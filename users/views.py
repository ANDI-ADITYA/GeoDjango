from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from maps.models import Polygon
from .forms import (
    UserRegisterForm,
    RawPolygonForm
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
    return render(request,'upload_Polygon.html', context)

