from rest_framework.routers import DefaultRouter
from thirds.api.views import ThirdApiViewSet


router_third = DefaultRouter()

router_third.register(
    prefix='thirds', basename='thirds', viewset=ThirdApiViewSet
)
