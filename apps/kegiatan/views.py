from django.shortcuts import render
from .models import Kegiatan


def kegiatan_index(request):
    upcoming = Kegiatan.objects.filter(is_published=True, is_arsip=False).order_by('-tanggal')
    arsip = Kegiatan.objects.filter(is_published=True, is_arsip=True).order_by('-tanggal')
    return render(request, 'kegiatan/index.html', {
        'upcoming': upcoming,
        'arsip': arsip,
    })
