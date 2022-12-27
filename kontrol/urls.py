from django.urls import path
from . import views
urlpatterns= [
path('', views.kimlik, name='kontrol'),

 ]