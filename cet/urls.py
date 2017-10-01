from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('inicio.urls')),
    url(r'^selecao/', include('selecao.urls')),
    url(r'^downloads/', include('downloads.urls')),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
