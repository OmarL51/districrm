from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from quotetypes.models import Quotety
from quotetypes.api.serializers import QuotetySerializer


class QuotetyApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = QuotetySerializer
    queryset = Quotety.objects.all()
