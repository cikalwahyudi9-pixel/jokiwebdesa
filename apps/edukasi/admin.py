from django.contrib import admin
from .models import KategoriEdukasi, ItemEdukasi


@admin.register(KategoriEdukasi)
class KategoriEdukasiAdmin(admin.ModelAdmin):
    list_display = ('nama', 'slug', 'urutan')
    list_editable = ('urutan',)
    prepopulated_fields = {'slug': ('nama',)}


@admin.register(ItemEdukasi)
class ItemEdukasiAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'pembuat', 'tanggal',
                    'jumlah_download', 'is_published')
    list_filter = ('kategori', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('judul', 'pembuat', 'program_asal')
    prepopulated_fields = {'slug': ('judul',)}
    readonly_fields = ('jumlah_download',)
