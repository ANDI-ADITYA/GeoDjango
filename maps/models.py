from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.utils.text import slugify
# Create your models here.

##------ POINT -------##
class Point(models.Model):
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=50)
	points = models.PointField(srid=4326)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Points" 

##------ POLYGON -------##
class Administrasi(models.Model):
	namobj = models.CharField(max_length=100)
	remark = models.CharField(max_length=250)
	lcode = models.CharField(max_length=20)
	wadmkk = models.CharField(max_length=100)
	wadmpr = models.CharField(max_length=100)
	wiadkk = models.CharField(max_length=100)
	shp_area = models.FloatField()
	shp = models.MultiPolygonField(srid=4326)

	def __unicode__(self):
		return self.namobj

		class Meta:
			ordering = ('namobj',)
			verbose_name_plural = "Administrasi"

## ------ STREET -------##
class Street(models.Model):
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=50)
	date = models.DateField()
	condition = models.CharField(max_length=100)
	lines = models.MultiLineStringField (srid=4326)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Street"