from django.contrib.gis import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from maps import views as maps_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('maps.urls'),name='pagemaps'),
    path('upload/point', user_views.uploadpoint, name='uploadpoint'),
	path('upload/polygon', user_views.uploadpolygon, name='uploadpolygon'),
    path('upload/street', user_views.uploadstreet, name='uploadstreet'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),

    path('update/point/<int:pk>', user_views.MapUpdateView.as_view(), name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
