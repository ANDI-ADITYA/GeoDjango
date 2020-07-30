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
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),

    path('point/', user_views.PointListView, name='list_point'),
    path('point/upload', user_views.uploadpoint, name='upload_point'),
    path('point/update/<int:pk>', user_views.PointAttrUpdateView.as_view(), name='attr_point'),
    path('point/delete/<int:pk>', user_views.PointDeleteView.as_view(),name='delete_point'),
    
    path('administrasi/', user_views.AdministrasiListView, name='list_administrasi'),
	path('administrasi/upload', user_views.uploadadministrasi, name='upload_administrasi'),
    path('administrasi/update/<int:pk>', user_views.AdministrasiAttrUpdateView.as_view(), name='attr_administrasi'),
    path('administrasi/delete/<int:pk>', user_views.AdministrasiDeleteView.as_view(),name='delete_administrasi'),
    
    path('street/', user_views.StreetListView, name='list_street'),
    path('street/upload', user_views.uploadstreet, name='upload_street'),
    path('street/update/<int:pk>', user_views.StreetAttrUpdateView.as_view(), name='attr_street'),
    path('street/delete/<int:pk>', user_views.StreetDeleteView.as_view(),name='delete_street'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
