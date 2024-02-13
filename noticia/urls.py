from django.contrib import admin
from django.urls import path, include
from noticia.views import noticias 

urlpatterns = [
    path("noticias/",noticias ),
    
]