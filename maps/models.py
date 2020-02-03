from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.utils.text import slugify
# Create your models here.

class Point(models.Model):
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=50)
	points = models.PointField(srid=4326)
	slug = models.SlugField(blank=True, editable=False)

	def save(self):
		self.slug = slugify(self.name)
		super().save()

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Points"


class Provinsi(models.Model):
	provinsi = models.CharField(max_length=255)
	sumber = models.CharField(max_length=255)
	polygon = models.MultiPolygonField(srid=4326)

	def __unicode__(self):
		return self.provinsi

	class Meta:
		verbose_name_plural = "Provinsi"
