# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('imagem', models.FileField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]