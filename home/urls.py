from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('maps.urls',namespace='maps')),
    path('admin/', admin.site.urls),
]
