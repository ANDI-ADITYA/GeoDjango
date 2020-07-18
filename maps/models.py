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
class Polygon(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	region = models.CharField(max_length=100)
	shp = models.MultiPolygonField(srid=4326)

	def __unicode__(self):
		return self.title

		class Meta:
			ordering = ('title',)
			verbose_name_plural = "Polygon"

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