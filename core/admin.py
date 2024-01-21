from django.contrib import admin
from .models import Cadastro
from django.contrib.auth.models import User

class CadastroAdmin(admin.ModelAdmin):
    #Mostra os CAMPOS desejados na rota 'admin/'
    list_display = ('nome', 'idade', 'sexo', 'cpf', 'profissao','email')
    list_display_links = ('nome','cpf','profissao','email')
    search_fields = ('nome','profissao')
    list_per_page = 15
    
    #Apresenta um filtro interativo pelos CAMPOS definidos
    list_filter = ('nome','profissao')
    
admin.site.register(Cadastro, CadastroAdmin)   
    
