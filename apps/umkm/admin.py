from django.contrib import admin
from .models import KategoriUMKM, UMKM, FotoUMKM, PendampinganBeforeAfter


class FotoUMKMInline(admin.TabularInline):
    model = FotoUMKM
    extra = 1
    fields = ('foto', 'caption', 'urutan')


class PendampinganInline(admin.TabularInline):
    model = PendampinganBeforeAfter
    extra = 1


@admin.register(KategoriUMKM)
class KategoriUMKMAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nama',)}


@admin.register(UMKM)
class UMKMAdmin(admin.ModelAdmin):
    list_display = ('nama_usaha', 'kategori', 'dusun', 'is_published',
                    'is_featured', 'izin_publikasi_kontak')
    list_filter = ('kategori', 'is_published', 'is_featured', 'izin_publikasi_kontak')
    list_editable = ('is_published', 'is_featured')
    search_fields = ('nama_usaha', 'nama_pemilik', 'dusun')
    prepopulated_fields = {'slug': ('nama_usaha',)}
    fieldsets = (
        ('Informasi Usaha', {
            'fields': ('nama_usaha', 'slug', 'nama_pemilik', 'kategori', 'dusun',
                       'deskripsi', 'produk_unggulan', 'foto_utama', 'logo')
        }),
        ('Kontak (Hanya tampil jika ada izin)', {
            'fields': ('izin_publikasi_kontak', 'kontak_wa', 'instagram',
                       'marketplace_url', 'google_maps_url', 'qris_image'),
            'classes': ('collapse',),
        }),
        ('Hasil Pendampingan KKN', {
            'fields': ('hasil_pendampingan',),
        }),
        ('Pengaturan Tampilan', {
            'fields': ('is_published', 'is_featured'),
        }),
    )
    inlines = [FotoUMKMInline, PendampinganInline]
