from django.db import models


class Kegiatan(models.Model):
    """
    Kegiatan/agenda desa dan program KKN.
    Sederhana — bukan sistem kalender kompleks.
    Tetap berguna sebagai arsip meski tidak ada pengelola aktif.
    """
    KATEGORI_CHOICES = [
        ('masyarakat', 'Kegiatan Masyarakat'),
        ('posyandu', 'Posyandu'),
        ('pemberdayaan', 'Pemberdayaan'),
        ('desa', 'Kegiatan Desa'),
        ('kkn', 'Program KKN'),
        ('lainnya', 'Lainnya'),
    ]
    judul = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True, max_length=320)
    tanggal = models.DateField()
    waktu = models.TimeField(null=True, blank=True)
    deskripsi = models.TextField(blank=True)
    lokasi = models.CharField(max_length=200, blank=True)
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES,
                                 default='lainnya')
    foto = models.ImageField(upload_to='kegiatan/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    is_arsip = models.BooleanField(default=False,
        help_text='Centang jika kegiatan sudah selesai (arsip)')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Kegiatan'
        verbose_name_plural = 'Kegiatan'
        ordering = ['-tanggal']

    def __str__(self):
        return f'{self.judul} — {self.tanggal}'

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(f'{self.judul}-{self.tanggal}')
        super().save(*args, **kwargs)
