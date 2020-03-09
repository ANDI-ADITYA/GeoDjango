from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from files import views as files_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('maps.urls'),name='pagemaps'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('shapefile/upload/', files_views.upload_shp, name='upload_shp'),
    path('shapefile/<int:pk>/', files_views.delete_shp, name='delete_shp'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
