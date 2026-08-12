from django.urls import path
from . import views

app_name = 'potensi'

urlpatterns = [
    path('', views.potensi_index, name='index'),
    path('<slug:slug>/', views.potensi_detail, name='detail'),
]
