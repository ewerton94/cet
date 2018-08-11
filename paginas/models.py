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

class Pagina(models.Model, UnicodePython2e3):
    titulo=models.CharField(max_length=200)
    url=models.CharField(max_length=200)
    ativa=models.BooleanField(max_length=200)
    nome_template=models.CharField(max_length=200)
    foto=models.FileField(upload_to='uploads/%Y/%m/%d/')
    def __unicode__(self):
        return self.titulo
    
