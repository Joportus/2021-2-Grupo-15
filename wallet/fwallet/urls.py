from django.urls import path
from . import views

urlpatterns = [
  path('walletv/', views.walletv, name='mi_wallet'),
]         