from django.urls import path
from . import views

urlpatterns = [
  path('walletv/', views.walletv, name='mi_wallet'),
  path('busqueda_registros/', views.filtrar_por, name='Busqueda de registros'),
  path('insertar_registro/', views.insertar_registros, name="ins_registro"),
  path('', views.inicio, name="inicio"),
  path('new/', views.ingresar_registro),
  path('register/',views.register_user, name = "register_user"),
  path('login/', views.login_user, name = "login"),
  path('logout',views.logout_user, name='logout'),
]         