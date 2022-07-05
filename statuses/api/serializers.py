from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from statuses.models import Status


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'tittle_s', 'color_s']
