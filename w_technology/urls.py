from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from core.urls import core_routes
from core.urls import api_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path(
        'api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include(core_routes.urls))
]

urlpatterns += api_docs_urls