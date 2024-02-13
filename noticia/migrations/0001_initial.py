# Generated by Django 4.2.9 on 2024-02-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Noticia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome_artigo",
                    models.CharField(max_length=100, verbose_name=" Nome do Artigo"),
                ),
                (
                    "artigo",
                    models.TextField(
                        blank=True, max_length=255, verbose_name="Artigos"
                    ),
                ),
                (
                    "data_artigo",
                    models.DateTimeField(auto_now=True, verbose_name="Data do Artigo"),
                ),
            ],
        ),
    ]
