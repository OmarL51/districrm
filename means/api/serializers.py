from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from means.models import Mean


class MeanSerializer(ModelSerializer):
    class Meta:
        model = Mean
        fields = ['id', 'tittle_m']
