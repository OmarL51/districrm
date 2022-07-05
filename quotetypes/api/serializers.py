from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from quotetypes.models import Quotety


class QuotetySerializer(ModelSerializer):
    class Meta:
        model = Quotety
        fields = ['id', 'tittle_q']
