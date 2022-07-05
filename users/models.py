from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Modelo de usuarios


class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Sustituimos el username por el email para iniciar sesion con el correo.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
