# Aqui definimos la ruta de nuestra API
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter

from users.api.views import UserApiViewSet, UserView

router_user = DefaultRouter()

# Registramos nuestras rutas
router_user.register(
    prefix='users', basename='users', viewset=UserApiViewSet

)

# Especificamos la ruta del usuario que no es admin
urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', UserView.as_view())
]
