from rest_framework import serializers
from .models import Usuario
from .models import CarregarRecarga



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 
                  'nome', 
                  'sobrenome', 
                  'telefone', 
                  'nif', 
                  'email', 
                  'endereco', 
                  'numero_de_conta',
                  'numero_do_contador',
                  'data_criacao']

class CarregarRecargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarregarRecarga
        fields = ['id', 
                  'id_do_usuario', 
                  'codigo_da_recarga', 
                  'data_criacao']