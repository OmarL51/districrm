from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from means_c.models import Mean_c
from means_c.api.serializers import MeanCSerializer


class MeanCApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MeanCSerializer
    queryset = Mean_c.objects.all()
