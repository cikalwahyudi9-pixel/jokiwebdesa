from django.contrib import admin
from .models import Kegiatan


@admin.register(Kegiatan)
class KegiatanAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal', 'kategori', 'lokasi', 'is_published', 'is_arsip')
    list_filter = ('kategori', 'is_published', 'is_arsip')
    list_editable = ('is_published', 'is_arsip')
    search_fields = ('judul', 'lokasi')
    prepopulated_fields = {'slug': ('judul',)}
    date_hierarchy = 'tanggal'
