from django.shortcuts import render, get_object_or_404
from .models import ProfilDesa, FasilitasDesa


def profil_index(request):
    """Halaman profil desa — menampilkan semua sub-informasi."""
    profil = ProfilDesa.objects.first()
    fasilitas = FasilitasDesa.objects.filter(is_published=True)
    return render(request, 'profil/index.html', {
        'profil': profil,
        'fasilitas': fasilitas,
    })
