from django.shortcuts import render, redirect
from .forms import ShapefileForm
from maps.models import shapefile



# Create your views here.
def upload_shp(request):
    if request.method == 'POST':
        form = ShapefileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maps:shapefile_list')
    else:
        form = ShapefileForm()

    return render(request, 'files/upload_shp.html', {
        'form': form
    })

def delete_shp(request, pk):
    if request.method == 'POST':
        shp = shapefile.objects.get(pk=pk)
        shp.delete()
    return redirect('maps:shapefile_list')
