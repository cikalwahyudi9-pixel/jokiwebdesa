from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit


class ProfilDesa(models.Model):
    """Model untuk profil/identitas dasar Desa Sumberagung."""
    nama_desa = models.CharField(max_length=200, default='Sumberagung')
    kecamatan = models.CharField(max_length=200, default='Weleri')
    kabupaten = models.CharField(max_length=200, default='Kendal')
    provinsi = models.CharField(max_length=200, default='Jawa Tengah')
    kode_pos = models.CharField(max_length=10, blank=True)
    luas_wilayah = models.CharField(max_length=100, blank=True,
                                     help_text='Contoh: 3,5 km²')
    jumlah_dusun = models.PositiveIntegerField(null=True, blank=True)
    koordinat_lat = models.DecimalField(max_digits=10, decimal_places=7,
                                         null=True, blank=True)
    koordinat_lng = models.DecimalField(max_digits=10, decimal_places=7,
                                         null=True, blank=True)
    deskripsi_singkat = models.TextField(blank=True,
        help_text='Deskripsi singkat untuk ditampilkan di Hero/Sekilas')
    sejarah = HTMLField(blank=True,
        help_text='Isi hanya jika data sejarah sudah divalidasi perangkat desa')
    kondisi_wilayah = HTMLField(blank=True)
    demografi = HTMLField(blank=True,
        help_text='Tampilkan hanya data yang diizinkan untuk dipublikasikan')
    foto_header = models.ImageField(upload_to='profil/', blank=True, null=True)
    video_file = models.FileField(upload_to='profil/video/', blank=True, null=True,
                                  help_text='Upload video profil (disarankan format MP4, maks 30MB)')
    video_youtube_url = models.URLField(blank=True,
                                        help_text='ATAU masukkan URL embed YouTube jika file video terlalu besar (akan diprioritaskan)')
    video_deskripsi = models.TextField(blank=True,
                                       help_text='Deskripsi singkat tentang video profil yang tampil di halaman video')
    video_sinopsis = models.TextField(blank=True,
                                      help_text='Sinopsis/ringkasan isi video profil (paragraf lebih panjang)')
    video_highlight = models.TextField(blank=True,
                                       help_text='Poin-poin highlight video, pisahkan dengan baris baru (Enter). Contoh: Potensi pertanian\nBudaya lokal\nKehidupan masyarakat')
    video_produksi = models.CharField(max_length=200, blank=True,
                                      help_text='Nama tim/pihak produksi video (misal: Tim KKN Undip 2026)')
    video_tahun = models.CharField(max_length=4, blank=True,
                                   help_text='Tahun produksi video (misal: 2026)')
    video_durasi = models.CharField(max_length=20, blank=True,
                                    help_text='Durasi video (misal: 5 menit 30 detik)')
    video_link = models.URLField(blank=True,
                                 help_text='Link video publik untuk dibagikan (YouTube, Google Drive, dll)')
    maps_embed_url = models.URLField(blank=True,
        help_text='URL embed Google Maps untuk desa')
    # Media Sosial
    sosmed_instagram = models.URLField(blank=True, help_text='URL profil Instagram (misal: https://instagram.com/desasumberagung)')
    sosmed_facebook = models.URLField(blank=True, help_text='URL halaman Facebook')
    sosmed_youtube = models.URLField(blank=True, help_text='URL channel YouTube')
    sosmed_whatsapp = models.CharField(max_length=20, blank=True, help_text='Nomor WhatsApp (format: 628xxxxxxxx)')
    sosmed_tiktok = models.URLField(blank=True, help_text='URL profil TikTok')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profil Desa'
        verbose_name_plural = 'Profil Desa'

    def __str__(self):
        return f'Desa {self.nama_desa}'

    def get_youtube_embed_url(self):
        """Mengubah link YouTube biasa menjadi format embed."""
        if not self.video_youtube_url:
            return ""
        
        url = self.video_youtube_url
        video_id = ""
        
        if "youtu.be/" in url:
            video_id = url.split("youtu.be/")[1][:11]
        elif "v=" in url:
            video_id = url.split("v=")[1][:11]
            
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return url


class FasilitasDesa(models.Model):
    """Fasilitas umum yang tersedia di desa."""
    KATEGORI_CHOICES = [
        ('pendidikan', 'Pendidikan'),
        ('kesehatan', 'Kesehatan'),
        ('ibadah', 'Ibadah'),
        ('pemerintahan', 'Pemerintahan'),
        ('olahraga', 'Olahraga'),
        ('lainnya', 'Lainnya'),
    ]
    nama = models.CharField(max_length=200)
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES)
    dusun = models.CharField(max_length=100, blank=True)
    keterangan = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Fasilitas Desa'
        verbose_name_plural = 'Fasilitas Desa'
        ordering = ['kategori', 'nama']

    def __str__(self):
        return self.nama
