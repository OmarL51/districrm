"""districrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Importamos nuestras rutas de la API users
from users.api.router import router_user
# Importamos nuestras rutas de la API incidencetypes
from incidencetypes.api.router import router_incidencety
# Importamos nuestras rutas de la API incidences
from incidences.api.router import router_incidence
# Importamos nuestras rutas de la API statuses
from statuses.api.router import router_status
# Importamos nuestras rutas de la API thirds
from thirds.api.router import router_third
# Importamos nuestras rutas de la API unexpecteds
from unexpecteds.api.router import router_unexpected
# Importamos nuestras rutas de la API means
from means.api.router import router_mean
# Importamos nuestras rutas de la API zones
from zones.api.router import router_zone
# Importamos nuestras rutas de la API quotes
from quotes.api.router import router_quote
# Importamos nuestras rutas de la API quotetypes
from quotetypes.api.router import router_quotety
# Importamos nuestras rutas de la API means_c
from means_c.api.router import router_mean_c


schema_view = get_schema_view(
    openapi.Info(
        title="DistriCRM - API",
        default_version='v1',
        description="Documentación de la API de DistriCRM",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Documentación de las APIs
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    # Rutas del usuario(normal)
    path('api/', include('users.api.router')),
    # Rutas de la api users(SuperUsuario)
    path('api/', include(router_user.urls)),
    # Rutas de la api incidencetypes(Tipos de incidencia)
    path('api/', include(router_incidencety.urls)),
    # Rutas de la api incidences(Incidencia)
    path('api/', include(router_incidence.urls)),
    # Rutas de la api statuses(Estados)
    path('api/', include(router_status.urls)),
    # Rutas de la api thirds(Terceros)
    path('api/', include(router_third.urls)),
    # Rutas de la api unexpecteds(Novedades)
    path('api/', include(router_unexpected.urls)),
    # Rutas de la api means(Medios)
    path('api/', include(router_mean.urls)),
    # Rutas de la api zones(Zonas)
    path('api/', include(router_zone.urls)),
    # Rutas de la api quotes(Cotizaciones)
    path('api/', include(router_quote.urls)),
    # Rutas de la api quotetypes(Tipos de cotizaciones)
    path('api/', include(router_quotety.urls)),
    # Rutas de la api means_c(Medios de cotizaciones)
    path('api/', include(router_quotety.urls)),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
