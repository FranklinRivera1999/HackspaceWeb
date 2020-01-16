from django.contrib import admin
from django.urls import path
from .views import HolaMundo, CrearCuenta, Publicaciones

urlpatterns = [
    path('inicio/', HolaMundo, name='index'),
    path('crearCuenta/', CrearCuenta),
    path('post/', Publicaciones)
]
