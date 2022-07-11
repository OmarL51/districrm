from django.contrib import admin
from means_c.models import Mean_c
# Register your models here.


@admin.register(Mean_c)
class MeanCAdmin(admin.ModelAdmin):
    pass
