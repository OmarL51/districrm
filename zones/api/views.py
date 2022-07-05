from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from zones.models import Zone
from zones.api.serializers import ZoneSerializer


class ZoneApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()
