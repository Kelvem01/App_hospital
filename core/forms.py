from django import forms

class CadastrarForm(forms.Form):
    nome = forms.CharField(label= 'Nome')
    idade = forms.IntegerField(label= 'Idade')
    sexo = forms.CharField(label= 'Sexo')
    cpf = forms.CharField(label='CPF')
    profissao = forms.CharField(label='Profissão')
    email = forms.EmailField(label= 'E-mail')