from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('tentang/', views.tentang, name='tentang'),
    path('video-profil/', views.video_profil, name='video_profil'),
    path('cari/', views.search, name='search'),
    path('kontribusi/', views.kontribusi, name='kontribusi'),
]
