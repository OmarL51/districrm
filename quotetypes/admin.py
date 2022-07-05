from django.contrib import admin
from quotetypes.models import Quotety
# Register your models here.


@admin.register(Quotety)
class QuotetyAdmin(admin.ModelAdmin):
    pass
