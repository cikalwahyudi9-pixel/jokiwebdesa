from django.db import models
from tinymce.models import HTMLField


class KategoriPotensi(models.Model):
    """Kategori potensi desa (Pertanian, Peternakan, UMKM, Budaya, dll)."""
    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    ikon = models.CharField(max_length=100, blank=True,
                             help_text='Nama ikon Bootstrap Icons, contoh: bi-leaf')
    deskripsi_singkat = models.TextField(blank=True)
    foto_cover = models.ImageField(upload_to='potensi/kategori/', blank=True, null=True)
    urutan = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Kategori Potensi'
        verbose_name_plural = 'Kategori Potensi'
        ordering = ['urutan', 'nama']

    def __str__(self):
        return self.nama


class ItemPotensi(models.Model):
    """Item/detail potensi dalam suatu kategori."""
    kategori = models.ForeignKey(KategoriPotensi, on_delete=models.CASCADE,
                                  related_name='items')
    judul = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    deskripsi = HTMLField(
        help_text='Hanya isi dengan data yang sudah diverifikasi dari lapangan')
    foto = models.ImageField(upload_to='potensi/items/', blank=True, null=True)
    sumber_data = models.CharField(max_length=200, blank=True,
                                    help_text='Sumber informasi data ini')
    is_published = models.BooleanField(default=True)
    urutan = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item Potensi'
        verbose_name_plural = 'Item Potensi'
        ordering = ['kategori', 'urutan', 'judul']

    def __str__(self):
        return f'{self.kategori.nama} — {self.judul}'
