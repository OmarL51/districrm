from rest_framework.routers import DefaultRouter
from quotetypes.api.views import QuotetyApiViewSet


router_quotety = DefaultRouter()

router_quotety.register(
    prefix='quotetypes', basename='quotetypes', viewset=QuotetyApiViewSet
)
