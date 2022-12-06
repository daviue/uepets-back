from rest_framework import serializers
from aplic.models import Pet, Usuario, Ong, Endereco, Vacina

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'nome', 'idade', 'raca', 'sexo', 'tipo', 'porte', 'pelo', 'descricao')

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','nome', 'email', 'senha', 'telefone', 'pet')

class OngsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ong
        fields = ('id','nome', 'email', 'senha', 'telefone', 'cnpj', 'pet')

class EnderecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'cep')

class VacinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = ('id','nome', 'data', 'pet')

