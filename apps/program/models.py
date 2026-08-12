from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify


class Program(models.Model):
    """
    Program pemberdayaan masyarakat yang dilaksanakan oleh tim KKN.

    Catatan: Halaman ini bernama 'Program Pemberdayaan', bukan 'Program KKN',
    agar website tidak terasa seperti dokumentasi KKN semata.
    """
    KATEGORI_CHOICES = [
        ('umkm', 'UMKM'),
        ('kesehatan', 'Kesehatan'),
        ('lingkungan', 'Lingkungan'),
        ('edukasi', 'Edukasi'),
        ('lainnya', 'Lainnya'),
    ]
    nama = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True, max_length=320)
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES)
    thumbnail = models.ImageField(upload_to='program/thumbnail/', blank=True, null=True)

    latar_belakang = HTMLField(blank=True)
    permasalahan = HTMLField(blank=True)
    tujuan = HTMLField(blank=True)
    sasaran = models.TextField(blank=True)
    pelaksanaan = HTMLField(blank=True)
    hasil = HTMLField(blank=True)
    dampak = HTMLField(blank=True)
    luaran = HTMLField(blank=True)

    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    urutan = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Program Pemberdayaan'
        verbose_name_plural = 'Program Pemberdayaan'
        ordering = ['kategori', 'urutan', 'nama']

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)


class DokumentasiProgram(models.Model):
    """Foto dokumentasi kegiatan program."""
    JENIS_CHOICES = [
        ('before', 'Sebelum'),
        ('after', 'Sesudah'),
        ('proses', 'Proses'),
        ('umum', 'Umum'),
    ]
    program = models.ForeignKey(Program, on_delete=models.CASCADE,
                                 related_name='dokumentasi')
    foto = models.ImageField(upload_to='program/dokumentasi/')
    caption = models.CharField(max_length=300, blank=True)
    jenis = models.CharField(max_length=20, choices=JENIS_CHOICES, default='umum')
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Dokumentasi Program'
        verbose_name_plural = 'Dokumentasi Program'
        ordering = ['urutan']

    def __str__(self):
        return f'{self.program.nama} — {self.get_jenis_display()} #{self.pk}'
