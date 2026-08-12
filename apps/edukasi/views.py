from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import KategoriEdukasi, ItemEdukasi


def edukasi_index(request):
    items = ItemEdukasi.objects.filter(is_published=True)
    kategori_list = KategoriEdukasi.objects.all()
    kategori_slug = request.GET.get('kategori')
    if kategori_slug:
        items = items.filter(kategori__slug=kategori_slug)
    return render(request, 'edukasi/index.html', {
        'items': items,
        'kategori_list': kategori_list,
        'filter_kategori': kategori_slug,
    })


def edukasi_download(request, slug):
    """Download file edukasi dan catat jumlah download."""
    item = get_object_or_404(ItemEdukasi, slug=slug, is_published=True)
    item.jumlah_download += 1
    item.save(update_fields=['jumlah_download'])
    return FileResponse(item.file_upload.open(), as_attachment=True,
                        filename=item.file_upload.name.split('/')[-1])
