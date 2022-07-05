from django.contrib import admin
from quotes.models import Quote
# Register your models here.


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    pass
