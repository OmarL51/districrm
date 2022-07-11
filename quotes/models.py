from django.db import models
# Create your models here.


class Quote(models.Model):
    date_cot = models.DateTimeField(null=True, blank=True)
    incidencety = models.ForeignKey(
        'incidencetypes.Incidencety', on_delete=models.SET_NULL, null=True, blank=True)
    quotety = models.ForeignKey(
        'quotetypes.Quotety', on_delete=models.SET_NULL, null=True, blank=True)
    tittle_cot = models.CharField(max_length=100)
    num_cot = models.IntegerField()
    line = models.IntegerField(default=0)
    assign = models.CharField(max_length=100)
    mean = models.ForeignKey(
        'means.Mean', on_delete=models.SET_NULL, null=True, blank=True)
    mean_c = models.ForeignKey(
        'means_c.Mean_c', on_delete=models.SET_NULL, null=True, blank=True)
    recotization = models.BooleanField()
    third = models.ForeignKey(
        'thirds.Third', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(
        'statuses.Status', on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey(
        'zones.Zone', on_delete=models.SET_NULL, null=True, blank=True)
    unexpected = models.ForeignKey(
        'unexpecteds.Unexpected', on_delete=models.SET_NULL, null=True, blank=True)
    # DEPENDE DEL TIPO DE COTIZACIÓN, SI ES CORRIENTE 1 DIA, SI ES CLIENTE NUEVO 3 DIAS Y SI ES PLATAFORMA SE DILIGENCIA MANUALMENTE
    date_ppta = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    observation = models.CharField(max_length=500)

    def __str__(self):
        return self.tittle_cot
