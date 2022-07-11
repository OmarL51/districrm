from rest_framework.routers import DefaultRouter
from means_c.api.views import MeanCApiViewSet


router_mean_c = DefaultRouter()

router_mean_c.register(
    prefix='means_c', basename='means_c', viewset=MeanCApiViewSet
)
