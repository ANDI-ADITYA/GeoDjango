from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.utils.text import slugify
# Create your models here.

##------ POINT -------##
class EduBuild(models.Model):
	namobj = models.CharField(max_length=100)
	remark = models.CharField(max_length=250)
	lcode = models.CharField(max_length=20)
	FGDPDK_CHOICES = (
		('College', 'College'),
		('Senior secondary Education (SMA, MA, SMALB)', 'Senior secondary Education (SMA, MA, SMALB)'),
		('Vocational secondary education (SMK, MAK)', 'Vocational secondary education (SMK, MAK)'),
		('First secondary education (SMP, MTs, SMPLB)', 'First secondary education (SMP, MTs, SMPLB)'),
		('Primary education (SD, MI, SDLB)', 'Primary education (SD, MI, SDLB)'),
		('Early childhood Education (TK, RA, TPA, KB)', 'Early childhood Education (TK, RA, TPA, KB)'),
		('Course Board', 'Course Board'),
		('Training Institute', 'Training Institute'),
		('Community Learning Activities Center', 'Community Learning Activities Center'),
		('Religious Education (Pesantren, Pasraman, etc.)', 'Religious Education (Pesantren, Pasraman, etc.)'),
		('Other', 'Other'),
	)
	fgdpdk = models.CharField(max_length=50, choices=FGDPDK_CHOICES)
	JNSPDK_CHOICES = (
		('General education', 'General education'),
		('Vocational education', 'Vocational education'),
		('Academic education', 'Academic education'),
		('Professional education', 'Professional education'),
		('Religious education', 'Religious education'),
		('Special education', 'Special education'),
		('Special Service Education', 'Special Service Education'),
		('Other', 'Other'),
	)
	jnspdk = models.CharField(max_length=30, choices=JNSPDK_CHOICES)
	points = models.PointField(srid=4326)

	def __unicode__(self):
		return self.namobj

	class Meta:
		ordering = ('namobj',)
		verbose_name_plural = "Education Building" 

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
	namrjl = models.CharField(max_length=100)
	lcode = models.CharField(max_length=20)
	SPCRJL_CHOICES = (
		('Freeway', 'Freeway'),
		('Highway', 'Highway'),
		('Moderate road', 'Moderate road'),
		('Small road', 'Small road'),
		('Other', 'Other'),
	)
	spcrjl = models.CharField(max_length=20, choices=SPCRJL_CHOICES)
	STARJL_CHOICES = (
		('Operational', 'Operational'),
		('Will be built', 'Will be built'),
		('Under construction', 'Under construction'),
		('No longer used', 'No longer used'),
		('Other', 'Other'),
	)
	starjl = models.CharField(max_length=20, choices=STARJL_CHOICES)
	UTKRJL_CHOICES = (
		('Public roads', 'Public roads'),
		('Special roads', 'Special roads'),
		('Other', 'Other'),
	)
	utkrjl = models.CharField(max_length=20, choices=UTKRJL_CHOICES)
	WLYRJL_CHOICES = (
		('Urban roads', 'Urban roads'),
		('Rural roads', 'Rural roads'),
		('Other', 'Other'),
	)
	wlyrjl = models.CharField(max_length=20, choices=WLYRJL_CHOICES)
	shp_length = models.FloatField()
	lines = models.MultiLineStringField (srid=4326)

	def __unicode__(self):
		return self.namrjl

	class Meta:
		ordering = ('utkrjl',)
		verbose_name_plural = "Street"