from django.db import models


class KategoriEdukasi(models.Model):
    """Kategori materi edukasi."""
    KATEGORI_CHOICES = [
        ('modul', 'Modul'),
        ('panduan', 'Panduan'),
        ('poster', 'Poster'),
        ('leaflet', 'Leaflet'),
        ('booklet', 'Booklet'),
        ('flashcard', 'Flashcard'),
        ('playbook', 'Playbook'),
        ('media', 'Media Edukasi'),
        ('lainnya', 'Lainnya'),
    ]
    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    ikon = models.CharField(max_length=100, blank=True,
                             help_text='Nama ikon Bootstrap Icons')
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Kategori Edukasi'
        verbose_name_plural = 'Kategori Edukasi'
        ordering = ['urutan', 'nama']

    def __str__(self):
        return self.nama


class ItemEdukasi(models.Model):
    """
    Materi edukasi yang dapat diunduh publik.
    Hanya tampilkan materi yang memang boleh dibagikan secara publik.
    """
    judul = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True, max_length=320)
    kategori = models.ForeignKey(KategoriEdukasi, on_delete=models.SET_NULL,
                                  null=True, blank=True, related_name='items')
    deskripsi = models.TextField(blank=True)
    pembuat = models.CharField(max_length=200, blank=True,
                                help_text='Nama pembuat/tim yang membuat materi')
    program_asal = models.CharField(max_length=200, blank=True,
                                     help_text='Program KKN asal materi ini')
    file_upload = models.FileField(upload_to='edukasi/files/')
    thumbnail = models.ImageField(upload_to='edukasi/thumbnail/', blank=True, null=True)
    tanggal = models.DateField(null=True, blank=True)
    jumlah_download = models.PositiveIntegerField(default=0, editable=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Item Edukasi'
        verbose_name_plural = 'Item Edukasi'
        ordering = ['-tanggal', 'judul']

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

    def get_format(self):
        """Mengembalikan format file (PDF, DOCX, dll)."""
        if self.file_upload:
            ext = self.file_upload.name.split('.')[-1].upper()
            return ext
        return ''

    def get_ukuran(self):
        """Mengembalikan ukuran file dalam format yang mudah dibaca."""
        try:
            size = self.file_upload.size
            if size < 1024:
                return f'{size} B'
            elif size < 1024 * 1024:
                return f'{size / 1024:.1f} KB'
            else:
                return f'{size / (1024 * 1024):.1f} MB'
        except Exception:
            return ''
