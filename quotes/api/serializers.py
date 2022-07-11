from dataclasses import fields
from rest_framework.serializers import ModelSerializer


from quotes.models import Quote
from incidencetypes.api.serializers import IncidencetySerializer
from statuses.api.serializers import StatusSerializer
from unexpecteds.api.serializers import UnexpectedSerializer
from thirds.api.serializers import ThirdSerializer
from means.api.serializers import MeanSerializer
from zones.api.serializers import ZoneSerializer
from quotetypes.api.serializers import QuotetySerializer
from means_c.api.serializers import MeanCSerializer


class QuoteSerializer(ModelSerializer):
    incidencety_data = IncidencetySerializer(
        source='incidencety', read_only=True)

    mean_data = MeanSerializer(
        source='mean', read_only=True)

    mean_c_data = MeanCSerializer(
        source='mean', read_only=True)

    unexpected_data = UnexpectedSerializer(
        source='unexpected', read_only=True)

    status_data = StatusSerializer(
        source='status', read_only=True)

    third_data = ThirdSerializer(
        source='third', read_only=True)

    zone_data = ZoneSerializer(
        source='zone', read_only=True)

    quotety_data = QuotetySerializer(
        source='quotety', read_only=True)

    class Meta:
        model = Quote
        fields = ['id', 'date_cot', 'incidencety',  'incidencety_data', 'quotety', 'quotety_data', 'tittle_cot', 'num_cot', 'line', 'assign', 'mean', 'mean_data', 'mean_c',  'mean_c_data', 'recotization', 'third', 'third_data', 'status', 'status_data', 'zone', 'zone_data',
                  'unexpected', 'unexpected_data', 'date_ppta',  'date', 'observation']
