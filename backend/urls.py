from django.urls import path
from django.conf.urls import include
from . import views
urlpatterns = [
	path('', views.Home.as_view(), name='home'),
	path('users/',include('django.contrib.auth.urls')),
	path('users/signup/', views.Register.as_view(), name='register'),
	path('users/login/', views.Login.as_view(), name='login'),
]
