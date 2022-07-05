from django.contrib import admin
from incidences.models import Incidence
# Register your models here.


@admin.register(Incidence)
class IncidenceAdmin(admin.ModelAdmin):
    pass
