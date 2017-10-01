# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Curso, Petiano, Sobre

class PetianoAdmin(admin.ModelAdmin):
    model = Petiano
    list_display = ['nome','curso']
    search_fields = ['nome']
    save_on_top = True
    
admin.site.register(Petiano,PetianoAdmin)
admin.site.register(Curso)
admin.site.register(Sobre)

