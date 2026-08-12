import json
from django.shortcuts import render
from .models import EventKesehatan


def insight_index(request):
    """Halaman Insight Kesehatan — data agregat + anonim + disclaimer wajib."""
    events = EventKesehatan.objects.filter(is_published=True).prefetch_related('data_agregat')

    # Statistik ringkasan
    total_events = events.count()
    total_peserta = sum(e.jumlah_peserta for e in events)

    # Serialize chart data per event untuk Chart.js
    chart_data = {}
    for event in events:
        from itertools import groupby
        data_list = list(event.data_agregat.all().order_by('indikator'))
        event_charts = {}
        for indikator, items in groupby(data_list, key=lambda x: x.indikator):
            items = list(items)
            event_charts[indikator] = {
                'label': items[0].get_indikator_display(),
                'labels': [i.label_nilai for i in items],
                'data': [i.jumlah for i in items],
                'persentase': [float(i.persentase) for i in items],
            }
        chart_data[event.pk] = event_charts

    context = {
        'events': events,
        'total_events': total_events,
        'total_peserta': total_peserta,
        'chart_data_json': json.dumps(chart_data),
    }
    return render(request, 'insight/index.html', context)
