from django.urls import path
from . import views

app_name = 'artikel'

urlpatterns = [
    path('', views.artikel_index, name='index'),
    path('<slug:slug>/', views.artikel_detail, name='detail'),
]
