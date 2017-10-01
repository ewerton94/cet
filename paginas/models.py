# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Pagina(models.Model):
    titulo=models.CharField(max_length=200)
    url=models.CharField(max_length=200)
    ativa=models.BooleanField(max_length=200)
    nome_template=models.CharField(max_length=200)
    foto=models.FileField(upload_to='uploads/%Y/%m/%d/')
    def __str__(self):
        return self.titulo
    
