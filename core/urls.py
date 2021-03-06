from django.conf.urls import url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from .views import ClientViewSet, EmpresaViewSet, LanceViewSet, OfertaViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

api_docs_urls = [
   url(
       r'^api/swagger(?P<format>\.json|\.yaml)$',
       schema_view.without_ui(cache_timeout=0),
       name='schema-json'
    ),
   url(
       r'^api/swagger/$',
       schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'
   ),
   url(
       r'^api/redoc/$',
       schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'
   ),
]


core_routes = routers.DefaultRouter()

core_routes.register('clientes', ClientViewSet)
core_routes.register('empresas', EmpresaViewSet)
core_routes.register('lances', LanceViewSet)
core_routes.register('ofertas', OfertaViewSet)
