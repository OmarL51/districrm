from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from thirds.models import Third


class ThirdSerializer(ModelSerializer):
    class Meta:
        model = Third
        fields = ['id', 'nit', 'nombres', 'contacto',
                  'correo', 'telefono', 'direccion', 'horario']
