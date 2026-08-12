from django.contrib import admin
from .models import Program, DokumentasiProgram


class DokumentasiInline(admin.TabularInline):
    model = DokumentasiProgram
    extra = 2
    fields = ('foto', 'caption', 'jenis', 'urutan')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kategori', 'is_published', 'is_featured', 'urutan')
    list_filter = ('kategori', 'is_published', 'is_featured')
    list_editable = ('is_published', 'is_featured', 'urutan')
    search_fields = ('nama',)
    prepopulated_fields = {'slug': ('nama',)}
    inlines = [DokumentasiInline]
    fieldsets = (
        ('Informasi Program', {
            'fields': ('nama', 'slug', 'kategori', 'thumbnail')
        }),
        ('Detail Program', {
            'fields': ('latar_belakang', 'permasalahan', 'tujuan', 'sasaran')
        }),
        ('Pelaksanaan & Hasil', {
            'fields': ('pelaksanaan', 'hasil', 'dampak', 'luaran')
        }),
        ('Pengaturan', {
            'fields': ('is_published', 'is_featured', 'urutan')
        }),
    )
