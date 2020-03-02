from django.urls import path
from .views import (
	HomePageView,  
	point_datasets, 
)

app_name='maps'

urlpatterns = [
	path('', HomePageView.as_view(),name='home'),	
	path('data-point/', point_datasets,name='data_point'),

]