# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Selecao
from inicio.views import add_contextos_gerais
from .forms import FormCandidato
from django.conf import settings
from django.contrib import messages
from unicodedata import normalize

def selecao(request):
    if request.method=="POST":
        for file in request.FILES:
            request.FILES[file].name=normalize('NFKD', request.FILES[file].name).encode('ASCII','ignore').decode('utf-8') 
        form = FormCandidato(request.POST, request.FILES)
        if form.is_valid():
            print('validado')
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Formulário enviado!\nObrigado por participar do nosso processo seletivo. Boa sorte!')
            return HttpResponseRedirect('%s/selecao/#inscricao'%settings.BASE_URL)
        else:
            print(form.errors)
            for erro in form.errors:
                messages.add_message(request, messages.ERROR, erro)
            return render(request,'index_selecao.html',add_contextos_gerais({'selecao':Selecao.objects.all()[0],'form':form}))          
    selecao = Selecao.objects.all()
    if selecao:
        selecao=selecao[0]
        if selecao.pagina.ativa:
            
            return render(request,'index_selecao.html',add_contextos_gerais({'selecao':selecao,'form':FormCandidato}))
        
    return HttpResponseRedirect('%s/selecao/#inscricao'%settings.BASE_URL)