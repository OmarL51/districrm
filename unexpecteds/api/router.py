from rest_framework.routers import DefaultRouter
from unexpecteds.api.views import UnexcpectedApiViewSet


router_unexpected = DefaultRouter()

router_unexpected.register(
    prefix='unexpecteds', basename='unexpecteds', viewset=UnexcpectedApiViewSet
)
