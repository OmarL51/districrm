from rest_framework.routers import DefaultRouter
from incidencetypes.api.views import IncidencetyApiViewSet


router_incidencety = DefaultRouter()

router_incidencety.register(
    prefix='incidencetypes', basename='incidencetypes', viewset=IncidencetyApiViewSet
)
