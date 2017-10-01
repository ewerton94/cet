# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Pasta(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    imagem = models.FileField(upload_to='uploads/%Y/%m/%d/')
    def __str__(self):
        return self.titulo
    
    
class Arquivo(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='uploads/%Y/%m/%d/')
    pasta = models.ForeignKey(Pasta)
    def __str__(self):
        return self.titulo
    
