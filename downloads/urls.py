# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url,include
from .views import download_arquivos

urlpatterns = [
    url(r'^(?P<pasta_id>[^/]+)/$', download_arquivos,name="downloads"),
]