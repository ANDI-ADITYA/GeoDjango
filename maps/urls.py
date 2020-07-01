from django.urls import path
from . import views as maps_views


app_name='maps'

urlpatterns = [
	path('', maps_views.HomePageView.as_view(), name='home-maps'),	
	path('data-point/', maps_views.point_datasets, name = 'data_point'),
	path('data-shape/', maps_views.shapefile_datasets, name='data_shape'),
	path('data-line/', maps_views.lines_datasets, name='data_line')

]