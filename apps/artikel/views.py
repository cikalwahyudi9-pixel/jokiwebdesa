from django.shortcuts import render, get_object_or_404
from .models import Artikel, KategoriArtikel


def artikel_index(request):
    """Daftar artikel dengan filter kategori."""
    artikel_list = Artikel.objects.filter(is_published=True)
    kategori_list = KategoriArtikel.objects.all()
    kategori_slug = request.GET.get('kategori')
    q = request.GET.get('q', '')

    if kategori_slug:
        artikel_list = artikel_list.filter(kategori__slug=kategori_slug)
    if q:
        artikel_list = artikel_list.filter(judul__icontains=q)

    return render(request, 'artikel/index.html', {
        'artikel_list': artikel_list,
        'kategori_list': kategori_list,
        'filter_kategori': kategori_slug,
        'query': q,
    })


def artikel_detail(request, slug):
    """Halaman detail artikel."""
    artikel = get_object_or_404(Artikel, slug=slug, is_published=True)
    related = Artikel.objects.filter(
        is_published=True, kategori=artikel.kategori
    ).exclude(pk=artikel.pk)[:3]
    return render(request, 'artikel/detail.html', {
        'artikel': artikel,
        'related': related,
    })
