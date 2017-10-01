# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Curso, Petiano, Sobre
from paginas.models import Pagina
from django.conf import settings
from .forms import SendEmail
from django.contrib import messages
from django.core.mail import send_mail
from downloads.models import Pasta

def add_contextos_gerais(contexto):
    contexto['BASE_URL']=settings.BASE_URL
    contexto['paginas_disponiveis']=Pagina.objects.filter(ativa=True)
    return contexto
def inicio(request):
    sobres = Sobre.objects.all().order_by('ordem')        
    petianos = Petiano.objects.all().order_by('nome')
    pastas = Pasta.objects.all()
    contexto = add_contextos_gerais({'page_url':'inicio','sobres':sobres,'petianos':petianos,'pastas':pastas})
    return render(request,'inicio.html',contexto)

def contato(request):
    if request.method == 'POST':
        print(request.POST)
        form = SendEmail(request.POST)
        if form.is_valid():
            print('form valido!!')
            solicitacao = form.cleaned_data
            sub = solicitacao['assunto']
            texto = [solicitacao['mensagem'],solicitacao['nome']]
            texto = '\n\nInteressado:'.join(texto)
            texto = [texto,solicitacao['email']]
            mes = '\n\nE-mail: '.join(texto)
            #mes = solicitacao['mensagem']
            from_email = settings.DEFAULT_FROM_EMAIL
            to_list = ['petct.ufal@gmail.com']
            send_mail(sub,mes,from_email,to_list,fail_silently=True)
        
            mensagem = 'Email enviado com sucesso!'
            messages.add_message(request, messages.SUCCESS, mensagem)
    return HttpResponseRedirect('%s/inicio/#contato'%settings.BASE_URL)
    