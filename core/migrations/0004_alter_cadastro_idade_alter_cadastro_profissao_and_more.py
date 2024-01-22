# Generated by Django 4.2.9 on 2024-01-22 22:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_cadastro_cadastrado_em_alter_cadastro_cpf_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cadastro",
            name="idade",
            field=models.CharField(max_length=10, verbose_name="Idade"),
        ),
        migrations.AlterField(
            model_name="cadastro",
            name="profissao",
            field=models.CharField(
                choices=[
                    ("todos", "Todos"),
                    ("anestesista", "Anestesista"),
                    ("cirurgião", "Cirurgiao"),
                    ("clinico geral", "Clinico Geral"),
                    ("cliente", "Cliente"),
                ],
                max_length=20,
                verbose_name="Profissão",
            ),
        ),
        migrations.AlterField(
            model_name="cadastro",
            name="sexo",
            field=models.CharField(
                choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outros")],
                max_length=20,
                verbose_name="Sexo",
            ),
        ),
    ]