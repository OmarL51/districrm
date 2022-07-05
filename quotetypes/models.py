from django.db import models

# Create your models here.


class Quotety(models.Model):
    tittle_q = models.CharField(max_length=100)

    def __str__(self):
        return self.tittle_q
