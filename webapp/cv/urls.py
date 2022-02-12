from django.urls import path
from .views import  aboutme, index, pic

app_name = 'cv'

urlpatterns = [
        path('', index, name='index'),
        path('aboutme/', aboutme.as_view(), name='aboutme'),
        path('pic/', pic.as_view(), name='pic'),

]