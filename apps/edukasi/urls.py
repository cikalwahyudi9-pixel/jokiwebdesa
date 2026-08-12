from django.urls import path
from . import views
app_name = 'edukasi'
urlpatterns = [
    path('', views.edukasi_index, name='index'),
    path('download/<slug:slug>/', views.edukasi_download, name='download'),
]
