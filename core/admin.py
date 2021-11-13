from django.contrib import admin

from .models import Cliente, Empresa, Lance, Oferta

# Register your models here.

admin.site.register([
    Empresa,
    Cliente,
    Oferta,
    Lance
])
