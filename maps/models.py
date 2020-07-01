from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.utils.text import slugify
# Create your models here.

class Point(models.Model):
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=50)
	points = models.PointField(srid=4326)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Points"

class Shapefile(models.Model):
	objname = models.CharField(max_length=100)
	wadmkk = models.CharField(max_length=100)
	wadmpr = models.CharField(max_length=100)
	shp = models.MultiPolygonField(srid=4326)

	def __unicode__(self):
		return self.objname

	class Meta:
		ordering = ('objname',)
		verbose_name_plural = "Shapefile"

class Lines(models.Model):
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=50)
	lines = models.LineStringField(srid=4326)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Lines"