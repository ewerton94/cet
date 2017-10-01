# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

class SendEmail(forms.Form):
    nome = forms.CharField(label="Nome",widget=forms.TextInput(attrs={'class':'inputFormulario','style':'font-family:futura;width:100%;'}))
    email = forms.EmailField(label = "E-mail",widget=forms.EmailInput(attrs={'class':'inputFormulario','style':'font-family:futura;'}))
    assunto = forms.CharField(label = "Assunto",widget=forms.TextInput(attrs={'class':'inputFormulario','style':'font-family:futura;'}))
    mensagem = forms.CharField(label = "mensagem", widget=forms.Textarea(attrs={'class':'inputFormulario','cols':'80','rows':'3','style':'font-family:futura;'}))