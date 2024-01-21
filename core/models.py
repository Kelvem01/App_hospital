from django.db import models

class Cadastro(models.Model):
    
    PREFERENCIA_SEXO_OPCOES =(
        ('M','Masculino'),
        ('F','Feminino'),
    )
    
    PREFERENCIA_PROFISSAO_POCAO=(
        ('todos','Todos'),
        ('anestesista','Anestesista'),
        ('cirurgião','Cirurgiao'),
        ('clinico geral','Clinico Geral'),
        ('cliente','Cliente'),
    )
    
    nome = models.CharField(verbose_name='Nome',max_length=200)
    idade = models.IntegerField(verbose_name='Idade')
    sexo = models.CharField(verbose_name='Sexo',max_length=20,
                            choices=PREFERENCIA_SEXO_OPCOES
    )
    cpf = models.CharField(verbose_name='CPF',max_length=11)
    profissao = models.CharField(verbose_name='Profissão',
                                 max_length=20,choices=PREFERENCIA_PROFISSAO_POCAO
    )
    email = models.CharField(verbose_name='E-mail',max_length=200)
    cadastrado_em = models.DateTimeField(verbose_name='Cadastrado em', auto_now=True)
     
     
    class META:
        db_table = 'cadastro'
        verbose_name = 'Cadastro'
        verbose_name_plural = 'Cadastros'