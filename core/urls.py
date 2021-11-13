from rest_framework import routers
from .views import ClientViewSet, EmpresaViewSet, LanceViewSet, OfertaViewSet


core_routes = routers.DefaultRouter()

core_routes.register('clientes', ClientViewSet)
core_routes.register('empresas', EmpresaViewSet)
core_routes.register('lances', LanceViewSet)
core_routes.register('ofertas', OfertaViewSet)
