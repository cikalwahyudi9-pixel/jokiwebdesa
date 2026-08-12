from django.shortcuts import render, get_object_or_404
from .models import Program


def program_index(request):
    program_list = Program.objects.filter(is_published=True).order_by('kategori', 'urutan')
    return render(request, 'program/index.html', {'program_list': program_list})


def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug, is_published=True)
    return render(request, 'program/detail.html', {'program': program})
