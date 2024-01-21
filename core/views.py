from django.shortcuts import render,  redirect
from core.forms import CadastrarForm

def base(request):
    return render(request, 'base.html')


def inicio(request):
    return render(request, 'inicio.html')


#add client on database
def cadastro(request):
    contexto = {'sucesso':False}
    form = CadastrarForm(request.POST or None)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        idade = form.cleaned_data['idade']
        sexo = form.cleaned_data['sexo']
        cpf = form.cleaned_data['cpf']
        profissao = form.cleaned_data['profissao']
        email = form.cleaned_data['email']
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'cadastro.html', {'form': form})