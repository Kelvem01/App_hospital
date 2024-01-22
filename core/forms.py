from django import forms
from core.models import Cadastro

class CadastrarForm(forms.ModelForm):
    
    class Meta:
        model = Cadastro
        fields =['nome','idade','sexo','cpf','profissao']
            