# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Pasta,Arquivo
from inicio.views import add_contextos_gerais
from django.conf import settings

def download_arquivos(request,pasta_id): 
    pasta = Pasta.objects.get(pk=int(pasta_id))
    arquivos = Arquivo.objects.filter(pasta=pasta)
    return render(request,'index_downloads.html',add_contextos_gerais({'pasta':pasta,'arquivos':arquivos}))
    