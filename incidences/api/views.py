from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from incidences.models import Incidence
from incidences.api.serializers import IncidenceSerializer


class IncidenceApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = IncidenceSerializer
    queryset = Incidence.objects.order_by('date').asc()
    # FILTROS
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'date', 'assign', 'order', 'rmv', 'third']
