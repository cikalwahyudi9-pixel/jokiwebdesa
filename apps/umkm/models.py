from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify


class KategoriUMKM(models.Model):
    """Kategori usaha UMKM."""
    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Kategori UMKM'
        verbose_name_plural = 'Kategori UMKM'
        ordering = ['nama']

    def __str__(self):
        return self.nama


class UMKM(models.Model):
    """
    Data UMKM mitra program pendampingan KKN.

    PENTING: Data ini adalah UMKM yang berpartisipasi dalam program KKN,
    bukan database seluruh UMKM Desa Sumberagung.
    Data kontak hanya dipublikasikan jika pemilik memberikan izin.
    """
    nama_usaha = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    nama_pemilik = models.CharField(max_length=200, blank=True)
    kategori = models.ForeignKey(KategoriUMKM, on_delete=models.SET_NULL,
                                  null=True, blank=True, related_name='umkm_list')
    dusun = models.CharField(max_length=100, blank=True)

    deskripsi = HTMLField(blank=True)
    produk_unggulan = models.TextField(blank=True,
                                        help_text='Produk-produk unggulan, pisahkan dengan koma')
    foto_utama = models.ImageField(upload_to='umkm/foto/', blank=True, null=True)
    logo = models.ImageField(upload_to='umkm/logo/', blank=True, null=True)

    # Kontak — hanya tampil jika ada izin
    izin_publikasi_kontak = models.BooleanField(default=False,
        help_text='Centang jika pemilik sudah memberikan izin publikasi kontak')
    kontak_wa = models.CharField(max_length=20, blank=True,
                                  help_text='Nomor WhatsApp tanpa awalan + atau 0')
    instagram = models.CharField(max_length=100, blank=True,
                                  help_text='Username Instagram tanpa @')
    marketplace_url = models.URLField(blank=True,
                                       help_text='URL toko di marketplace (Shopee, Tokopedia, dll)')
    google_maps_url = models.URLField(blank=True)
    qris_image = models.ImageField(upload_to='umkm/qris/', blank=True, null=True)

    # Hasil pendampingan KKN
    hasil_pendampingan = HTMLField(blank=True,
        help_text='Ceritakan hasil pendampingan: branding, kemasan, QRIS, dll')

    is_published = models.BooleanField(default=False,
        help_text='Centang untuk menampilkan di website')
    is_featured = models.BooleanField(default=False,
        help_text='Centang untuk ditampilkan di halaman Home')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'UMKM Mitra'
        verbose_name_plural = 'UMKM Mitra'
        ordering = ['nama_usaha']

    def __str__(self):
        return self.nama_usaha

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama_usaha)
        super().save(*args, **kwargs)


class FotoUMKM(models.Model):
    """Galeri foto produk/kegiatan UMKM."""
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE,
                              related_name='foto_galeri')
    foto = models.ImageField(upload_to='umkm/galeri/')
    caption = models.CharField(max_length=200, blank=True)
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Foto UMKM'
        verbose_name_plural = 'Foto UMKM'
        ordering = ['urutan']

    def __str__(self):
        return f'Foto {self.umkm.nama_usaha} #{self.pk}'


class PendampinganBeforeAfter(models.Model):
    """Dokumentasi before-after hasil pendampingan UMKM."""
    JENIS_CHOICES = [
        ('branding', 'Branding/Logo'),
        ('kemasan', 'Kemasan'),
        ('label', 'Label Produk'),
        ('qris', 'QRIS'),
        ('digital', 'Digital Marketing'),
        ('katalog', 'Katalog'),
        ('lainnya', 'Lainnya'),
    ]
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE,
                              related_name='pendampingan')
    jenis = models.CharField(max_length=50, choices=JENIS_CHOICES)
    foto_sebelum = models.ImageField(upload_to='umkm/before/', blank=True, null=True)
    foto_sesudah = models.ImageField(upload_to='umkm/after/', blank=True, null=True)
    keterangan = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Pendampingan Before-After'
        verbose_name_plural = 'Pendampingan Before-After'

    def __str__(self):
        return f'{self.umkm.nama_usaha} — {self.get_jenis_display()}'
