# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url,include
from .views import inicio,contato
urlpatterns = [
    url(r'^$', inicio,name='inicio'),
    url(r'^contato/$', contato,name='contato'),
]
