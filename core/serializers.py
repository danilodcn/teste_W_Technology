from rest_framework import serializers
from .models import Cliente, Empresa, Lance, Oferta


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class LanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lance
        fields = '__all__'


class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'
