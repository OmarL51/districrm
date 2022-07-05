from dataclasses import fields
from rest_framework.serializers import ModelSerializer


from zones.models import Zone


class ZoneSerializer(ModelSerializer):

    class Meta:
        model = Zone
        fields = ['id', 'zona', 'asesor']
