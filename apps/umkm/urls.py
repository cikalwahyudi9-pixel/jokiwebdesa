from django.urls import path
from . import views

app_name = 'umkm'

urlpatterns = [
    path('', views.umkm_index, name='index'),
    path('<slug:slug>/', views.umkm_detail, name='detail'),
]
