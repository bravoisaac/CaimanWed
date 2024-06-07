from django.urls import path
from .views import usuarios, detalleusuario

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', usuarios, name='usuarios'),
    path('detalleusuario', detalleusuario, name='detalleusuario')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)