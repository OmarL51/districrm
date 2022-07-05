from dataclasses import fields
from rest_framework.serializers import ModelSerializer


from incidences.models import Incidence
from incidencetypes.api.serializers import IncidencetySerializer
from statuses.api.serializers import StatusSerializer
from unexpecteds.api.serializers import UnexpectedSerializer
from thirds.api.serializers import ThirdSerializer
from means.api.serializers import MeanSerializer


class IncidenceSerializer(ModelSerializer):
    incidencety_data = IncidencetySerializer(
        source='incidencety', read_only=True)

    mean_data = MeanSerializer(
        source='mean', read_only=True)

    unexpected_data = UnexpectedSerializer(
        source='unexpected', read_only=True)

    status_data = StatusSerializer(
        source='status', read_only=True)

    third_data = ThirdSerializer(
        source='third', read_only=True)

    class Meta:
        model = Incidence
        fields = ['id', 'date_oc',  'incidencety',  'incidencety_data', 'tittle', 'mean', 'mean_data', 'status', 'status_data', 'date', 'assign', 'order', 'line',
                  'rmv', 'unexpected', 'unexpected_data', 'oc_client', 'date_rmv', 'third', 'third_data']
