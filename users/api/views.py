from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from users.models import User
from users.api.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    # Definimos quien tendra permiso o acceso sobre la API en este caso un usuario administrador
    permission_classes = [IsAdminUser]
    # El serializador es para definir como queremos que nos devuelvan los datos
    serializer_class = UserSerializer
    # El queryset es a que modelo tenemos que apuntar o atacar
    queryset = User.objects.all()

    # Override del create para encriptar la contraseña cuando creemos un usuario
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    # Override del update para encriptar la contraseña cuando actualizamos un usuario
    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        # si el usuario actualiza la contraseña
        if password:
            request.data['password'] = make_password(password)
        # si el usuario no actualiza la contraseña
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)


#  El usuario hace una peticion y obtiene sus propios datos
class UserView(APIView):
    # Definimos quien tendra permiso o acceso sobre la API en este caso un usuario autenticado o ensesión
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
