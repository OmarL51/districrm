from rest_framework.routers import DefaultRouter
from incidences.api.views import IncidenceApiViewSet


router_incidence = DefaultRouter()

router_incidence.register(
    prefix='incidences', basename='incidences', viewset=IncidenceApiViewSet
)
