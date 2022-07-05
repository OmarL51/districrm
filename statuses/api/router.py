from rest_framework.routers import DefaultRouter
from statuses.api.views import StatusApiViewSet


router_status = DefaultRouter()

router_status.register(
    prefix='statuses', basename='statuses', viewset=StatusApiViewSet
)
