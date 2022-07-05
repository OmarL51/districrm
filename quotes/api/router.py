from rest_framework.routers import DefaultRouter
from quotes.api.views import QuoteApiViewSet


router_quote = DefaultRouter()

router_quote.register(
    prefix='quotes', basename='quotes', viewset=QuoteApiViewSet
)
