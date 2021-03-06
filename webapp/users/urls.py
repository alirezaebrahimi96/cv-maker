from django.urls import path, include
from . import views
app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('password/', views.change_password, name='change_password'),
]