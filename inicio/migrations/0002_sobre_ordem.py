# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobre',
            name='ordem',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
