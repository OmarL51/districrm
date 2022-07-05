from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from unexpecteds.models import Unexpected


class UnexpectedSerializer(ModelSerializer):
    class Meta:
        model = Unexpected
        fields = ['id', 'tittle_u', 'color_u']
