from django.db import models

# Create your models here.


class Unexpected(models.Model):
    tittle_u = models.CharField(max_length=100)
    color_u = models.CharField(max_length=100, default='#fff')

    def __str__(self):
        return self.tittle_u
