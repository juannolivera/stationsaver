from django.contrib import admin
from .models import Surtidor, Transaccion  # Asegúrate de importar tus modelos

admin.site.register(Surtidor)  # Registra el modelo Surtidor
admin.site.register(Transaccion)  # Registra el modelo Transaccion
