from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from thirds.models import Third
from thirds.api.serializers import ThirdSerializer


class ThirdApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ThirdSerializer
    queryset = Third.objects.all()
