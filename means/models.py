from django.db import models

# Create your models here.


class Mean(models.Model):
    tittle_m = models.CharField(max_length=100)

    def __str__(self):
        return self.tittle_m
