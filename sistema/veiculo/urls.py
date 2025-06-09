from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='veiculo'),
    path('listar/', VeiculoListView.as_view(), name='listar_veiculo'),
    path('criar/', login_required(VeiculoCreateView.as_view(),login_url=''), name='criar_veiculo'),
    path('editar/<int:pk>/', login_required(VeiculoEditView.as_view(), login_url=''), name='editar_veiculo'),
    path('deletar/<int:pk>/', login_required(VeiculoDeleteView.as_view(), login_url=''), name='deletar_veiculo'),
    # path('listar_alt/', ListarViewAlt.as_view(), name='listar_veiculo_alt'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto_veiculo'),
    path('api/listar/', VeiculoAPIListar.as_view(), name='api_listar_veiculo'),
]