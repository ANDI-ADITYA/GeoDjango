from django.urls import path
from . import views as maps_views


app_name='maps'

urlpatterns = [
	path('', maps_views.HomePageView.as_view(), name='home-maps'),	
	path('data-point/', maps_views.point_datasets, name = 'data_points'),
	path('data-poly/', maps_views.polygon_datasets, name='data_poly'),
	path('data-street/', maps_views.street_datasets, name='data_street')

]