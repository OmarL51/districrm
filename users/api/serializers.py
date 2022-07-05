from rest_framework import serializers
from users.models import User

# clase del serializador


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Modelo que usaremos
        model = User
        # Fields que devolveremos
        fields = ['id', 'username', 'password',
                  'email', 'is_active', 'is_staff']
