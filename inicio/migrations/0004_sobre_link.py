# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-11 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_petiano_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobre',
            name='link',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]