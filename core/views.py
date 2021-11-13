from rest_framework import permissions, viewsets

from .models import Cliente, Empresa, Lance, Oferta

from .serializers import (
    ClientSerializer, EmpresaSerializer,
    LanceSerializer, OfertaSerializer
)


class ClientViewSet(viewsets.ModelViewSet):
    """
    Endpoint usado para gerenciar o model Client
    """
    queryset = Cliente.objects.all()
    serializer_class = ClientSerializer
    permission_class = [permissions.IsAuthenticated]


class EmpresaViewSet(viewsets.ModelViewSet):
    """
    Endpoint usado para gerenciar o model Empresa
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_class = [permissions.IsAuthenticated]


class OfertaViewSet(viewsets.ModelViewSet):
    """
    Endpoint usado para gerenciar o model Oferta
    """
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    permission_class = [permissions.IsAuthenticated]


class LanceViewSet(viewsets.ModelViewSet):
    """
    Endpoint usado para gerenciar o model Lance
    """
    queryset = Lance.objects.all()
    serializer_class = LanceSerializer
    permission_class = [permissions.IsAuthenticated]
