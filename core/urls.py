from django.contrib import admin
from django.urls import path, include
from .views import  base , inicio, cadastro , listar,noticias



urlpatterns = [
    
    path('',base,name='base'),
    path('inicio/',inicio, name='inicio'),
    path('cadastro/',cadastro, name='cadastro'),
    path('listar/',listar, name='listar'),
    path('noticias/',noticias,name='noticias'),
    
]
