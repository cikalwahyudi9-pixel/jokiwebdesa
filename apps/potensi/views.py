from django.shortcuts import render, get_object_or_404
from .models import KategoriPotensi, ItemPotensi


def potensi_index(request):
    """Halaman utama potensi desa."""
    kategori_list = KategoriPotensi.objects.filter(is_published=True).order_by('urutan')
    return render(request, 'potensi/index.html', {'kategori_list': kategori_list})


def potensi_detail(request, slug):
    """Detail potensi per kategori."""
    kategori = get_object_or_404(KategoriPotensi, slug=slug, is_published=True)
    items = ItemPotensi.objects.filter(kategori=kategori, is_published=True).order_by('urutan')
    return render(request, 'potensi/detail.html', {'kategori': kategori, 'items': items})
