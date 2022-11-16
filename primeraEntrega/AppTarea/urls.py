from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('crear_curso', crear_curso),
    path('buscar_curso/', buscar_curso),
    path('crear_edificio', crear_edificio),
    path('buscar_edificio', buscar_edificio),
    path('crear_aula', crear_aula),
    path('buscar_aula', buscar_aula),
]