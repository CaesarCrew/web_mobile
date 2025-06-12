from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Veiculo
from .forms import formulario_veiculo
from .consts import OPCOES_COMBUSTIVEIS, OPCOES_MARCAS, OPCOES_CORES
from .serializers import VeiculoSerializer

from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class IndexView (View):
    def get(self, request):
        return render(request, 'index.html')

class VeiculoCreateView (LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = formulario_veiculo
    template_name = 'criar.html'
    success_url = reverse_lazy('listar_veiculo')

class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'listar.html'
    context_object_name = 'veiculos'

class VeiculoEditView (LoginRequiredMixin,UpdateView):
    model = Veiculo
    form_class = formulario_veiculo
    context_object_name = 'veiculos'
    template_name = 'editar.html'
    success_url = reverse_lazy('listar_veiculo')

class VeiculoDeleteView(LoginRequiredMixin, DeleteView):
    model = Veiculo
    template_name = 'alert.html'
    success_url = reverse_lazy("listar_veiculo")

class FotoVeiculo(View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            return Http404('<h1>Veículo não encontrado</h1>')

class VeiculoAPIListar(ListAPIView):
    serializer_class = VeiculoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()

class VeiculoAPIDelete(DeleteView):
    model = Veiculo
    serializer_class = VeiculoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        try:
            veiculo = self.get_object()
            veiculo.delete()
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response(status=404)
