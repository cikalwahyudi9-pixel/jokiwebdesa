from django.contrib import admin
from .models import KategoriGaleri, ItemGaleri


@admin.register(KategoriGaleri)
class KategoriGaleriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'slug', 'urutan')
    list_editable = ('urutan',)
    prepopulated_fields = {'slug': ('nama',)}


@admin.register(ItemGaleri)
class ItemGaleriAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'tanggal', 'is_published', 'is_featured')
    list_filter = ('kategori', 'is_published', 'is_featured')
    list_editable = ('is_published', 'is_featured')
    search_fields = ('judul', 'deskripsi')
