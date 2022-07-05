from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from means.models import Mean
from means.api.serializers import MeanSerializer


class MeanApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MeanSerializer
    queryset = Mean.objects.all()
