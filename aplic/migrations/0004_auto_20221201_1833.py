# Generated by Django 2.2.19 on 2022-12-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_auto_20221201_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='ong',
            name='cnpj',
            field=models.IntegerField(max_length=14),
        ),
        migrations.AlterField(
            model_name='ong',
            name='telefone',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.IntegerField(max_length=20),
        ),
    ]
