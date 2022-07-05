from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from statuses.models import Status
from statuses.api.serializers import StatusSerializer


class StatusApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
