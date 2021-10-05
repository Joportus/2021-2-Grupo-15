from django.urls import path
from . import views

urlpatterns = [
  path('walletv/', views.walletv, name='mi_wallet'),
  path('busqueda_registros/', views.busqueda_registros, name='Busqueda de registros'),
  path('buscar/', views.buscarMonto),
  path('insertar_registro/', views.insertar_registros, name="ins_registro"),
  path('inicio/', views.inicio),
]         