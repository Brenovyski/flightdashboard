from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("crud", views.crud, name="crud"),
    path("enhanced_crud", views.enhanced_crud, name="enhanced_crud"),
    path("gera_relatorio", views.gera_relatorio, name="gera_relatorio"),
    path("painel", views.painel.as_view(), name="painel"),
    path("painel2", views.painel2.as_view(), name="painel2"),

    path("voos", views.voos.as_view(), name="voos"),
    path("atualiza_status", views.atualiza_status, name="atualiza_status"),
    path("criar_voo", views.criar_voo, name="criar_voo"),
    path("editar_voo", views.editar_voo, name="editar_voo"),
    path("ler_voo", views.ler_voo, name="ler_voo"),
    path("deletar_voo", views.deletar_voo, name="deletar_voo"),
    path("relatorio_chegadas", views.relatorio_chegadas, name="relatorio_chegadas"),
    path("relatorio_partidas", views.relatorio_partidas, name="relatorio_partidas"),
]