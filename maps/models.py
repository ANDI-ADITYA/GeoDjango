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

class shapefile(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	shp = models.FileField(upload_to='shps/')

	def __str__(self):
		return self.title

	def delete(self, *args, **kwargs):
		self.shp.delete()
		super().delete(*args, **kwargs)	
