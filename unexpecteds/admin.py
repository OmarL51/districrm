from django.contrib import admin
from unexpecteds.models import Unexpected
# Register your models here.


@admin.register(Unexpected)
class UnexpectedAdmin(admin.ModelAdmin):
    pass
