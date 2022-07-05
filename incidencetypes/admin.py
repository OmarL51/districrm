from django.contrib import admin
from incidencetypes.models import Incidencety
# Register your models here.


@admin.register(Incidencety)
class IncidencetyAdmin(admin.ModelAdmin):
    pass
