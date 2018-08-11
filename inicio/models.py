# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

import sys

class UnicodePython2e3(object):
    if sys.version_info[0] >= 3: # Python 3
        def __str__(self):
            return self.__unicode__()
    else:  # Python 2
        def __str__(self):
            return self.__unicode__().encode('utf8')

class Sobre(models.Model, UnicodePython2e3):
    nome = models.CharField(max_length=200)
    foto = models.FileField(upload_to='uploads/%Y/%m/%d/')
    descricao = models.TextField()
    ordem =  models.IntegerField()
    link = models.CharField(max_length=400, null=True, blank=True)
    def __unicode__(self):
        return self.nome
    
    @property
    def eh_par(self):
        return self.ordem%2==0 

    
class Curso(models.Model, UnicodePython2e3):
    nome = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nome

class Petiano(models.Model, UnicodePython2e3):
    nome = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso)
    periodo = models.IntegerField()
    foto = models.FileField(upload_to='uploads/%Y/%m/%d/')
    def __unicode__(self):
        return self.nome
