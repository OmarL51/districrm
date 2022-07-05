from django.contrib import admin
from means.models import Mean
# Register your models here.


@admin.register(Mean)
class MeanAdmin(admin.ModelAdmin):
    pass
