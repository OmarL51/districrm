from django.db import models
# Create your models here.


class Incidence(models.Model):
    date_oc = models.DateTimeField(null=True, blank=True)
    incidencety = models.ForeignKey(
        'incidencetypes.Incidencety', on_delete=models.SET_NULL, null=True, blank=True)
    tittle = models.CharField(max_length=100)
    oc_client = models.CharField(max_length=100)
    mean = models.ForeignKey(
        'means.Mean', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(
        'statuses.Status', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    assign = models.CharField(max_length=100)
    order = models.IntegerField()
    line = models.IntegerField(default=0)
    rmv = models.IntegerField()
    unexpected = models.ForeignKey(
        'unexpecteds.Unexpected', on_delete=models.SET_NULL, null=True, blank=True)
    date_rmv = models.DateTimeField(null=True, blank=True)
    third = models.ForeignKey(
        'thirds.Third', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.tittle
