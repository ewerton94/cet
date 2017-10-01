# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from paginas.models import Pagina

class Selecao(models.Model):
    class Meta:
        verbose_name = "Seleção"
        verbose_name_plural = "Seleção"
    descricao = models.CharField(max_length=200)
    periodo = models.CharField(max_length=200)
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField()
    pagina = models.ForeignKey(Pagina)
    foto = models.FileField(upload_to='uploads/%Y/%m/%d/')
    edital = models.FileField(upload_to='uploads/%Y/%m/%d/')
    def __str__(self):
        return self.descricao
    

    
class Candidato(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateTimeField()
    naturalidade = models.CharField(max_length=200)
    estado_civil = models.CharField(max_length=200)
    rg = models.CharField(max_length=200)
    arquivorg = models.FileField(upload_to='uploads/%Y/%m/%d/')
    cpf = models.CharField(max_length=200)
    arquivocpf = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True)
    endereco = models.CharField(max_length=200)
    mora_com = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    foto = models.FileField(upload_to='uploads/%Y/%m/%d/')
    local = models.CharField(max_length=200)
    certificado = models.FileField(upload_to='uploads/%Y/%m/%d/')
    matricula = models.IntegerField()
    comprovante_matricula = models.FileField(upload_to='uploads/%Y/%m/%d/')
    curso = models.CharField(max_length=200)
    periodo = models.CharField(max_length=200)
    historico = models.FileField(upload_to='uploads/%Y/%m/%d/')
    atividade = models.CharField(max_length=300,blank=True)
    bolsa = models.CharField(max_length=300,blank=True)
    projeto = models.CharField(max_length=300,blank=True)
    orientador = models.CharField(max_length=300,blank=True)

'''Local e ano que concluiu o ensino médio
Conclusão ensino médio
Matrícula
Curso
Semestre
Endereço
Mora com
Ativisade remunerada
Qual?
Recebe bolsa ou auxílio da ufal
Qual
Participa projeto pesquisa
Título projeto
Orientador
Comprovante de matrícula
Histórico analítico

'''