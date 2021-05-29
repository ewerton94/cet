# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-19 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0007_auto_20200519_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='internet',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Tem problema com internet'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='atendimento_especial',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
