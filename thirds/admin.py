from django.contrib import admin
from thirds.models import Third
# Register your models here.


@admin.register(Third)
class ThirdAdmin(admin.ModelAdmin):
    pass
