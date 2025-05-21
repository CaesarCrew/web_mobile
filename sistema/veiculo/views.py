from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Veiculo
from .forms import formulario_veiculo
from .consts import OPCOES_COMBUSTIVEIS, OPCOES_MARCAS, OPCOES_CORES

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class VeiculoView(CreateView):
    model = Veiculo
    form_class = formulario_veiculo
    template_name = 'criar.html'
    success_url = reverse_lazy('listar_veiculo')

class ListarView(ListView):
    model = Veiculo
    template_name = 'listar.html'
    context_object_name = 'veiculos'

class FotoVeiculo(View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            return Http404('<h1>Veículo não encontrado</h1>')