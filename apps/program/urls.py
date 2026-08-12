from django.urls import path
from . import views
app_name = 'program'
urlpatterns = [
    path('', views.program_index, name='index'),
    path('<slug:slug>/', views.program_detail, name='detail'),
]
