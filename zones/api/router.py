from rest_framework.routers import DefaultRouter
from zones.api.views import ZoneApiViewSet


router_zone = DefaultRouter()

router_zone.register(
    prefix='zones', basename='zones', viewset=ZoneApiViewSet
)
