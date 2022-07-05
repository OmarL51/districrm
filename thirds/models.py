from django.db import models

# Create your models here.


class Third(models.Model):
    nit = models.IntegerField()
    nombres = models.CharField(max_length=200)
    contacto = models.CharField(max_length=200, default="")
    correo = models.EmailField(unique=True, default="")
    telefono = models.CharField(max_length=50, default="")
    direccion = models.CharField(max_length=500, default="")
    horario = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.nombres
