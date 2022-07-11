from django.db import models

# Create your models here.


class Mean_c(models.Model):
    tittle_mc = models.CharField(max_length=100)

    def __str__(self):
        return self.tittle_mc
