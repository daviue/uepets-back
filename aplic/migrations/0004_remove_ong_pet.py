# Generated by Django 2.2.19 on 2022-12-01 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_auto_20221130_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ong',
            name='pet',
        ),
    ]