from django.db import models

# Create your models here.
class shapefile(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    region = models.CharField(max_length=150)
    shp = models.FileField(upload_to='files/shapefile/')

    def __str__(self):
        return self.title

class raster(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    region = models.CharField(max_length=150)
    geotiff = models.FileField(upload_to='files/raster/')

    def __str__(self):
        return self.title