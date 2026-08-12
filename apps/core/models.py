from django.db import models


class Kontribusi(models.Model):
    """Form kontribusi/masukan dari pengunjung atau warga."""
    JENIS_CHOICES = [
        ('cerita', 'Cerita / Pengalaman'),
        ('masukan', 'Masukan / Saran'),
        ('koreksi', 'Koreksi Informasi'),
        ('lainnya', 'Lainnya'),
    ]
    nama = models.CharField(max_length=200, help_text='Nama pengirim (boleh nama samaran)')
    email = models.EmailField(blank=True, help_text='Email opsional, untuk kami menghubungi balik')
    jenis = models.CharField(max_length=20, choices=JENIS_CHOICES, default='masukan')
    pesan = models.TextField(help_text='Tulis cerita atau masukan Anda')
    is_approved = models.BooleanField(default=False, help_text='Centang untuk menampilkan ke publik')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Kontribusi'
        verbose_name_plural = 'Kontribusi Masyarakat'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_jenis_display()} dari {self.nama} ({self.created_at.strftime("%d %b %Y")})'
