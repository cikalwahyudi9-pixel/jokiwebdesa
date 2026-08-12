from django.db import models


class KategoriGaleri(models.Model):
    """Kategori galeri foto."""
    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Kategori Galeri'
        verbose_name_plural = 'Kategori Galeri'
        ordering = ['urutan', 'nama']

    def __str__(self):
        return self.nama


class ItemGaleri(models.Model):
    """
    Item foto di galeri.
    Foto harus dikompresi sebelum diupload agar website tidak berat.
    """
    foto = models.ImageField(upload_to='galeri/')
    judul = models.CharField(max_length=200, blank=True)
    deskripsi = models.TextField(blank=True)
    kategori = models.ForeignKey(KategoriGaleri, on_delete=models.SET_NULL,
                                  null=True, blank=True, related_name='items')
    tanggal = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False,
        help_text='Centang untuk tampil di halaman Home')
    urutan = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Item Galeri'
        verbose_name_plural = 'Item Galeri'
        ordering = ['-created_at', 'urutan']

    def __str__(self):
        return self.judul or f'Foto #{self.pk}'
