# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0002_auto_20170716_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data', models.DateTimeField()),
                ('naturalidade', models.CharField(max_length=200)),
                ('estado_civil', models.CharField(max_length=200)),
                ('rg', models.CharField(max_length=200)),
                ('arquivorg', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('cpf', models.CharField(max_length=200)),
                ('arquivocpf', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('email', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('foto', models.FileField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]
