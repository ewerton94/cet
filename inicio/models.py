# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Sobre(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.FileField(upload_to='uploads/%Y/%m/%d/')
    descricao = models.TextField()
    ordem =  models.IntegerField()
    def __str__(self):
        return self.nome
    
    @property
    def eh_par(self):
        return self.ordem%2==0 

    
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Petiano(models.Model):
    nome = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso)
    periodo = models.IntegerField()
    foto = models.FileField(upload_to='uploads/%Y/%m/%d/')
    def __str__(self):
        return self.nome
