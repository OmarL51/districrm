from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from unexpecteds.models import Unexpected
from unexpecteds.api.serializers import UnexpectedSerializer


class UnexcpectedApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UnexpectedSerializer
    queryset = Unexpected.objects.all()
