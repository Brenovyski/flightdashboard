from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("crud", views.crud, name="crud"),
    path("gera_relatorio", views.gera_relatorio, name="gera_relatorio"),
    path("atualiza_status", views.atualiza_status, name="atualiza_status")
]