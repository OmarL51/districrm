from django.contrib import admin
from statuses.models import Status
# Register your models here.


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
