from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

from .models import Ricetta, Ingrediente, IngredientiRicette

admin.site.register(Ricetta)
admin.site.register(Ingrediente)
admin.site.register(IngredientiRicette)

