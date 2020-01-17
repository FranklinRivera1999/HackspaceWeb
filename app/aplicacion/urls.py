from django.contrib import admin
from django.urls import path
from .views import HolaMundo, CrearCuenta, Publicaciones, addComent, myPosts, editQuestion

urlpatterns = [
    path('inicio/', HolaMundo, name='index'),
    path('crearCuenta/', CrearCuenta),
    path('post/', Publicaciones),
    path('comentario/', addComent),
    path('mispublicaciones/', myPosts),
    path('editQuestion/', editQuestion)
]
