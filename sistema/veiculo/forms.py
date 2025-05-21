from django import forms
from .models import Veiculo
from .consts import *

class formulario_veiculo(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'marca', 'cor', 'ano', 'combustivel', 'foto']

