from django.urls import path
from . import views

urlpatterns = [
    path('', views.fad_list, name='fad_list'),
    path('decades/', views.decade_list, name='decade_list'),
    path('fad/<int:pk>', views.fad_detail, name = 'fad_detail'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail')
]