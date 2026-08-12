from django.shortcuts import render, get_object_or_404
from .models import UMKM, KategoriUMKM


def umkm_index(request):
    """Daftar UMKM mitra program KKN dengan filter kategori & dusun."""
    umkm_list = UMKM.objects.filter(is_published=True)
    kategori_list = KategoriUMKM.objects.all()

    # Filter
    kategori_slug = request.GET.get('kategori')
    dusun = request.GET.get('dusun')
    q = request.GET.get('q', '')

    if kategori_slug:
        umkm_list = umkm_list.filter(kategori__slug=kategori_slug)
    if dusun:
        umkm_list = umkm_list.filter(dusun__icontains=dusun)
    if q:
        umkm_list = umkm_list.filter(nama_usaha__icontains=q)

    dusun_list = UMKM.objects.filter(is_published=True).values_list('dusun', flat=True).distinct()

    return render(request, 'umkm/index.html', {
        'umkm_list': umkm_list,
        'kategori_list': kategori_list,
        'dusun_list': [d for d in dusun_list if d],
        'filter_kategori': kategori_slug,
        'filter_dusun': dusun,
        'query': q,
    })


def umkm_detail(request, slug):
    """Halaman detail UMKM."""
    umkm = get_object_or_404(UMKM, slug=slug, is_published=True)
    pendampingan = umkm.pendampingan.all()
    foto_galeri = umkm.foto_galeri.all()
    umkm_lain = UMKM.objects.filter(
        is_published=True, kategori=umkm.kategori
    ).exclude(pk=umkm.pk)[:3]

    return render(request, 'umkm/detail.html', {
        'umkm': umkm,
        'pendampingan': pendampingan,
        'foto_galeri': foto_galeri,
        'umkm_lain': umkm_lain,
    })
