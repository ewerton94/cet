# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Pagina

class PaginaAdmin(admin.ModelAdmin):
    model = Pagina
    list_display = ['titulo','ativa']
    search_fields = ['titulo']
    save_on_top = True
    
admin.site.register(Pagina,PaginaAdmin)

