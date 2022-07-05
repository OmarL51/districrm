from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# Register your models here.


# Decorador
@admin.register(User)
# En esta clase pasamos el modelo del usuario
class UserAdmin(BaseUserAdmin):
    pass
