from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

from apps.artikel.models import Artikel
from apps.umkm.models import UMKM
from apps.potensi.models import KategoriPotensi, ItemPotensi
from apps.galeri.models import ItemGaleri
from apps.program.models import Program
from apps.edukasi.models import ItemEdukasi
from apps.kegiatan.models import Kegiatan
from apps.profil.models import ProfilDesa
from apps.core.models import Kontribusi


def home(request):
    """Halaman utama / Home."""
    context = {
        'artikel_terbaru': Artikel.objects.filter(is_published=True).order_by('-tanggal_publish')[:4],
        'umkm_featured': UMKM.objects.filter(is_published=True, is_featured=True)[:4],
        'potensi_kategori': KategoriPotensi.objects.filter(is_published=True).order_by('urutan')[:4],
        'galeri_featured': ItemGaleri.objects.filter(is_published=True, is_featured=True)[:8],
        'program_featured': Program.objects.filter(is_published=True, is_featured=True)[:3],
        'edukasi_terbaru': ItemEdukasi.objects.filter(is_published=True).order_by('-tanggal')[:3],
    }
    return render(request, 'pages/home.html', context)


def tentang(request):
    """Halaman Tentang Website."""
    return render(request, 'pages/tentang.html')


def video_profil(request):
    """Halaman Video Profil Desa."""
    profil = ProfilDesa.objects.first()
    return render(request, 'pages/video_profil.html', {'profil': profil})


def search(request):
    """Pencarian lintas konten."""
    query = request.GET.get('q', '').strip()
    results = {}
    total = 0

    if query:
        artikel = Artikel.objects.filter(
            is_published=True
        ).filter(Q(judul__icontains=query) | Q(isi__icontains=query))[:6]

        umkm = UMKM.objects.filter(
            is_published=True
        ).filter(Q(nama_usaha__icontains=query) | Q(deskripsi__icontains=query))[:6]

        potensi = ItemPotensi.objects.filter(
            is_published=True
        ).filter(Q(judul__icontains=query) | Q(deskripsi__icontains=query))[:6]

        edukasi = ItemEdukasi.objects.filter(
            is_published=True
        ).filter(Q(judul__icontains=query) | Q(deskripsi__icontains=query))[:6]

        kegiatan = Kegiatan.objects.filter(
            is_published=True
        ).filter(Q(judul__icontains=query) | Q(deskripsi__icontains=query))[:6]

        results = {
            'Artikel': {'items': artikel, 'url_name': 'artikel:detail', 'slug_field': 'slug'},
            'UMKM': {'items': umkm, 'url_name': 'umkm:detail', 'slug_field': 'slug'},
            'Potensi': {'items': potensi, 'url_name': 'potensi:item_detail', 'slug_field': 'slug'},
            'Edukasi': {'items': edukasi, 'url_name': None, 'slug_field': 'slug'},
            'Kegiatan': {'items': kegiatan, 'url_name': None, 'slug_field': 'slug'},
        }
        total = sum(r['items'].count() for r in results.values())

    return render(request, 'pages/search.html', {
        'query': query,
        'results': results,
        'total': total,
    })


def kontribusi(request):
    """Halaman form kontribusi masyarakat."""
    if request.method == 'POST':
        nama = request.POST.get('nama', '').strip()
        email = request.POST.get('email', '').strip()
        jenis = request.POST.get('jenis', 'masukan')
        pesan = request.POST.get('pesan', '').strip()
        honeypot = request.POST.get('website', '')  # spam protection

        if honeypot:
            return redirect('pages:kontribusi')

        if nama and pesan:
            Kontribusi.objects.create(
                nama=nama, email=email, jenis=jenis, pesan=pesan
            )
            messages.success(request, 'Terima kasih! Kontribusi Anda telah kami terima dan akan ditinjau oleh tim.')
            return redirect('pages:kontribusi')
        else:
            messages.error(request, 'Nama dan pesan wajib diisi.')

    kontribusi_publik = Kontribusi.objects.filter(is_approved=True)[:5]
    return render(request, 'pages/kontribusi.html', {
        'kontribusi_publik': kontribusi_publik,
    })
