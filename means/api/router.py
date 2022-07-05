from rest_framework.routers import DefaultRouter
from means.api.views import MeanApiViewSet


router_mean = DefaultRouter()

router_mean.register(
    prefix='means', basename='means', viewset=MeanApiViewSet
)
