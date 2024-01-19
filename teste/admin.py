from django.contrib import admin
from .models import Carro


class CarroAdmin(admin.ModelAdmin):
    ...

admin.site.register(Carro, CarroAdmin)