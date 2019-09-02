# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from .models import Candidato

class FormCandidato(ModelForm):
    class Meta:
        model=Candidato
        fields=[
            'nome','nome_social','data','naturalidade','estado_civil','rg','arquivorg','cpf','arquivocpf','endereco','mora_com','email','telefone','foto','reserva_de_vagas', 'atendimento_especial',
            'local','situacao_projeto','certificado','matricula','comprovante_matricula','curso','periodo','historico','atividade','bolsa','projeto','orientador',
            'comprovante_cad_unico', 'auto_declaracao', 'necessita_atendimento_especial'
            
        ]
