from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from incidencetypes.models import Incidencety


class IncidencetySerializer(ModelSerializer):
    class Meta:
        model = Incidencety
        fields = ['id', 'tittle']
