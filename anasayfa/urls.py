from django.urls import path

from . import views

urlpatterns = [
    # ex: /anasayfa/
    path('', views.anasayfayz, name='anasayfayz'),


]
