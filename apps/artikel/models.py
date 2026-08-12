from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify


class KategoriArtikel(models.Model):
    """Kategori artikel/berita."""
    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    warna_label = models.CharField(max_length=50, default='success',
        help_text='Warna Bootstrap: success, primary, warning, info, danger, secondary')

    class Meta:
        verbose_name = 'Kategori Artikel'
        verbose_name_plural = 'Kategori Artikel'
        ordering = ['nama']

    def __str__(self):
        return self.nama


class Artikel(models.Model):
    """Artikel/berita tentang Desa Sumberagung dan program KKN."""
    judul = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True, max_length=320)
    thumbnail = models.ImageField(upload_to='artikel/thumbnail/', blank=True, null=True)
    kategori = models.ForeignKey(KategoriArtikel, on_delete=models.SET_NULL,
                                  null=True, blank=True, related_name='artikel')
    penulis = models.CharField(max_length=200, blank=True)
    tanggal_publish = models.DateField()
    isi = HTMLField()
    ringkasan = models.TextField(max_length=300, blank=True,
                                  help_text='Ringkasan singkat untuk kartu artikel (maks 300 karakter)')
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False,
        help_text='Centang untuk ditampilkan di Home')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Artikel'
        verbose_name_plural = 'Artikel'
        ordering = ['-tanggal_publish']

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)
