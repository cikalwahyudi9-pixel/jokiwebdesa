from django.shortcuts import render
from .models import KategoriGaleri, ItemGaleri


def galeri_index(request):
    """Halaman galeri foto dengan filter kategori."""
    galeri_list = ItemGaleri.objects.filter(is_published=True)
    kategori_list = KategoriGaleri.objects.all()
    kategori_slug = request.GET.get('kategori')

    if kategori_slug:
        galeri_list = galeri_list.filter(kategori__slug=kategori_slug)

    return render(request, 'galeri/index.html', {
        'galeri_list': galeri_list,
        'kategori_list': kategori_list,
        'filter_kategori': kategori_slug,
    })
