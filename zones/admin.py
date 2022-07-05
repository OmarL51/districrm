from django.contrib import admin
from zones.models import Zone
# Register your models here.


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    pass
