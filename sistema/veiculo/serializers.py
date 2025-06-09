from rest_framework import serializers
from .models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    nome_marca = serializers.SerializerMethodField()
    nome_cor = serializers.SerializerMethodField()
    nome_combustivel = serializers.SerializerMethodField()

    class Meta:
        model = Veiculo
        exclude = []

    def get_nome_marca(self, obj):
        return obj.get_marca_display()
    
    def get_nome_cor(self, obj):
        return obj.get_cor_display()
    
    def get_nome_combustivel(self, obj):
        return obj.get_combustivel_display()