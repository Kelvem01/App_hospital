from django.db import models

class Noticia(models.Model):
    nome_artigo = models.CharField(verbose_name=" Nome do Artigo" , max_length=100)
    artigo = models.TextField(verbose_name="Artigos" , max_length=255)
    data_artigo = models.DateTimeField(verbose_name="Data do Artigo", auto_now=True)
    
    class META:
        db_table = 'noticia'
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
