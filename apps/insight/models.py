from django.db import models


class EventKesehatan(models.Model):
    """
    Event/kegiatan Posyandu atau skrining kesehatan.

    PENTING - ATURAN PRIVASI:
    - Hanya data AGREGAT yang boleh ditampilkan
    - TIDAK BOLEH ada nama, NIK, atau identitas individu
    - WAJIB ada disclaimer di halaman Insight
    - Data tidak merepresentasikan kondisi seluruh masyarakat desa
    """
    nama_kegiatan = models.CharField(max_length=300)
    tanggal = models.DateField()
    dusun = models.CharField(max_length=100)
    jumlah_peserta = models.PositiveIntegerField()
    rentang_usia = models.CharField(max_length=100, blank=True,
                                     help_text='Contoh: 45–80 tahun')
    catatan = models.TextField(blank=True,
        help_text='Catatan umum kegiatan, bukan data individual')
    disclaimer_text = models.TextField(
        default=(
            'Data pada bagian ini merupakan ringkasan hasil kegiatan/skrining '
            'peserta program dan tidak merepresentasikan kondisi kesehatan '
            'seluruh masyarakat Desa Sumberagung. Informasi ditampilkan untuk '
            'tujuan dokumentasi dan edukasi, bukan sebagai diagnosis medis.'
        ),
        help_text='Disclaimer wajib tampil di halaman Insight Kesehatan'
    )
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Event Kesehatan'
        verbose_name_plural = 'Event Kesehatan'
        ordering = ['-tanggal']

    def __str__(self):
        return f'{self.nama_kegiatan} — {self.tanggal}'


class DataAgregatKesehatan(models.Model):
    """
    Data agregat hasil skrining kesehatan.
    Semua data bersifat statistik, BUKAN data individual.
    """
    INDIKATOR_CHOICES = [
        ('tekanan_darah', 'Tekanan Darah'),
        ('gula_darah', 'Gula Darah'),
        ('kolesterol', 'Kolesterol'),
        ('asam_urat', 'Asam Urat'),
        ('berat_badan', 'Berat Badan / IMT'),
        ('lainnya', 'Lainnya'),
    ]
    event = models.ForeignKey(EventKesehatan, on_delete=models.CASCADE,
                               related_name='data_agregat')
    indikator = models.CharField(max_length=50, choices=INDIKATOR_CHOICES)
    label_nilai = models.CharField(max_length=100,
        help_text='Contoh: Normal, Pra-Hipertensi, Hipertensi Stage 1')
    jumlah = models.PositiveIntegerField()
    keterangan = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Data Agregat Kesehatan'
        verbose_name_plural = 'Data Agregat Kesehatan'
        ordering = ['event', 'indikator']

    def __str__(self):
        return f'{self.event} — {self.get_indikator_display()}: {self.label_nilai}'

    @property
    def persentase(self):
        """Hitung persentase dari total peserta event."""
        if self.event.jumlah_peserta > 0:
            return round((self.jumlah / self.event.jumlah_peserta) * 100, 1)
        return 0
