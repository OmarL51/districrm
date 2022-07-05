from django.db import models

# Create your models here.


class Status(models.Model):
    tittle_s = models.CharField(max_length=100)
    color_s = models.CharField(max_length=100, default='#fff')

    def __str__(self):
        return self.tittle_s
