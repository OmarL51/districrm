from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer


class QuoteApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
