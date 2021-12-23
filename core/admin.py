from django.contrib import admin

from .models import Clientes, Medicos

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone',)
    
@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    list_display = ('nome',)
