"""
Jelajah Sumberagung — URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    # Pages
    path('', include('apps.pages.urls')),

    # Main sections
    path('profil/', include('apps.profil.urls')),
    path('potensi/', include('apps.potensi.urls')),
    path('umkm/', include('apps.umkm.urls')),
    path('artikel/', include('apps.artikel.urls')),
    path('galeri/', include('apps.galeri.urls')),
    path('program/', include('apps.program.urls')),
    path('edukasi/', include('apps.edukasi.urls')),
    path('insight/', include('apps.insight.urls')),
    path('kegiatan/', include('apps.kegiatan.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
