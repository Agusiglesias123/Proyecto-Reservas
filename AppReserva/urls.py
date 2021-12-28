from django.contrib import admin
from django.urls import path

from .import views


urlpatterns = [
    path('', views.index, name="index.html"),
    path('galeria/', views.galeria, name="galeria.html"),
    path('gestion/', views.gestion, name="gestion.html"),

]