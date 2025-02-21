from .views import *
from django.urls import path


urlpatterns = [
    path('api/get',lista_categorias,name='lista'),
    path('ver/',ver_categorias,name='ver'),
    path('agregar/',agregar_categoria,name='agregar')
]