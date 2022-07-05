from django.db import models
# Create your models here.


class Zone(models.Model):
    zona = models.CharField(max_length=100)
    asesor = models.CharField(max_length=100)

    def __str__(self):
        return self.asesor
