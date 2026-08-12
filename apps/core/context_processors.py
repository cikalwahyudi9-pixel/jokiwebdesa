"""
Context processors untuk template global.
Menyediakan variabel site_info yang tersedia di semua template.
"""

from django.conf import settings
from apps.profil.models import ProfilDesa


def site_info(request):
    profil = ProfilDesa.objects.first()

    nama = profil.nama_desa if profil else 'Sumberagung'
    kecamatan = profil.kecamatan if profil else 'Weleri'
    kabupaten = profil.kabupaten if profil else 'Kendal'
    provinsi = profil.provinsi if profil else 'Jawa Tengah'

    return {
        'site_name': f'Jelajah {nama}',
        'site_tagline': f'Satu Ruang untuk Mengenal {nama}',
        'site_core_message': 'Discover the place. Explore the potential. Connect with the community.',
        'desa_nama': f'Desa {nama}',
        'desa_kecamatan': f'Kecamatan {kecamatan}',
        'desa_kabupaten': f'Kabupaten {kabupaten}',
        'desa_provinsi': provinsi,
        'disclaimer_resmi': (
            f'Website ini bukan merupakan website resmi Pemerintah Desa {nama} '
            'dan tidak menyediakan layanan administrasi pemerintahan desa. '
            f'Jelajah {nama} adalah platform informasi mandiri yang dikembangkan '
            'sebagai salah satu luaran program KKN Universitas Diponegoro 2026.'
        ),
        'google_analytics_id': getattr(settings, 'GOOGLE_ANALYTICS_ID', ''),
        'profil': profil,
    }
