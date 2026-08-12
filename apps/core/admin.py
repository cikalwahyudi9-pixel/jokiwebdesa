from django.contrib import admin
from .models import Kontribusi


@admin.register(Kontribusi)
class KontribusiAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis', 'created_at', 'is_approved')
    list_filter = ('jenis', 'is_approved')
    list_editable = ('is_approved',)
    search_fields = ('nama', 'pesan')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
