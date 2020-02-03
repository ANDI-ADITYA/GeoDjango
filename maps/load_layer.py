import os
from django.contrib.gis.utils import LayerMapping
from .models import GOWA

gowa_mapping = {
    'namobj': 'NAMOBJ',
    'wadmkk': 'WADMKK',
    'wadmpr': 'WADMPR',
    'stsdrh': 'STSDRH',
    'stsdat': 'STSDAT',
    'nothpr': 'NOTHPR',
    'geom': 'MULTIPOLYGON',
}

gowa_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/GOWA.shp'))

def run(verbose=True):
	lm = LayerMapping(GOWA,gowa_shp,gowa_mapping, transform = False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)