from django.shortcuts import render,  redirect
from core.forms import CadastrarForm 
from core.models import Cadastro
from noticia.models import Noticia

def base(request):
    return render(request, 'inicio.html')


def inicio(request):
    return render(request, 'inicio.html')


#add client on database
def cadastro(request):
    contexto = {'sucesso':False}
    form = CadastrarForm(request.POST or None)
    if form.is_valid():
        form.save()
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'cadastro.html', contexto)

def listar(request):
    pessoas = Cadastro.objects.all()
    return render(request,'listar.html',{"pessoas":pessoas})