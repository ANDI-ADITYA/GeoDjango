from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('maps.urls'),name='pagemaps'),
	path('upload', user_views.upload, name='upload'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),

]


