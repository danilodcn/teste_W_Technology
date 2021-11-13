from rest_framework import viewsets
from rest_framework import permissions

import serializers
import models


class ClientViewSet(viewsets.ModelViewSet):
    """
    Endpoint usado para gerenciar o model Client
    """
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_class = [permissions.IsAuthenticated]


class EmpresaViewSet(viewsets.ModelViewSet):
    """
    Endpoint usado para gerenciar o model Empresa
    """
    queryset = models.Empresa.objects.all()
    serializer_class = serializers.EmpresaSerializer
    permission_class = [permissions.IsAuthenticated]


class OfertaViewSet(viewsets.ModelViewSet):
    """
    Endpoint usado para gerenciar o model Oferta
    """
    queryset = models.Oferta.objects.all()
    serializer_class = serializers.OfertaSerializer
    permission_class = [permissions.IsAuthenticated]


class LanceViewSet(viewsets.ModelViewSet):
    """
    Endpoint usado para gerenciar o model Lance
    """
    queryset = models.Lance.objects.all()
    serializer_class = serializers.LanceSerializer
    permission_class = [permissions.IsAuthenticated]
