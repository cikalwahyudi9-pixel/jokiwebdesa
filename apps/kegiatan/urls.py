from django.urls import path
from . import views
app_name = 'kegiatan'
urlpatterns = [path('', views.kegiatan_index, name='index')]
