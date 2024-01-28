from django.contrib import admin
from django.urls import path, include
from .views import  base , inicio, cadastro


urlpatterns = [
    
    path('',base,name='base'),
    path('inicio/',inicio, name='inicio'),
    path('cadastro/',cadastro, name='cadastro'),
    
]
