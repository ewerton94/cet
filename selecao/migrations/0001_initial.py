# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selecao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('periodo', models.CharField(max_length=200)),
                ('data_inicio', models.DateTimeField()),
                ('data_final', models.DateTimeField()),
                ('foto', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('edital', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('pagina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.Pagina')),
            ],
        ),
    ]
