from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='veiculo'),
    path('criar/', VeiculoView.as_view(), name='criar_veiculo'),
    path('listar/', ListarView.as_view(), name='listar_veiculo'),
    # path('listar_alt/', ListarViewAlt.as_view(), name='listar_veiculo_alt'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto_veiculo'),
]