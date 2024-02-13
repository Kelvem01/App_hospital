from django.shortcuts import render

def noticias(request):
    return render(request,"noticia.html")
