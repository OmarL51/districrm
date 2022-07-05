from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from incidencetypes.models import Incidencety
from incidencetypes.api.serializers import IncidencetySerializer


class IncidencetyApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = IncidencetySerializer
    queryset = Incidencety.objects.all()
