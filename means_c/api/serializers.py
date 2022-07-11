from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from means_c.models import Mean_c


class MeanCSerializer(ModelSerializer):
    class Meta:
        model = Mean_c
        fields = ['id', 'tittle_mc']
