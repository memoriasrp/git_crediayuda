from django.contrib import admin
from .models import * 
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    #list_display =('title', 'order')

admin.site.register(Clientes, ClientesAdmin)

class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    search_fields = ('descripcion',)
    ordering = ['-id']
    #list_display =('title', 'order')

admin.site.register(EstadoCivil, EstadoCivilAdmin)


class BancoAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    search_fields = ('descripcion',)
    ordering = ['-id']
    #list_display =('title', 'order')

admin.site.register(Banco, BancoAdmin)

class CompaniaCelAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    search_fields = ('descripcion',)
    ordering = ['-id']
    #list_display =('title', 'order')

admin.site.register(CompaniaCel, CompaniaCelAdmin)


class TipoDireccionAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    search_fields = ('descripcion',)
    ordering = ['-id']
    #list_display =('title', 'order')

admin.site.register(TipoDireccion, TipoDireccionAdmin)


class TipoTelefonoAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    search_fields = ('descripcion',)
    ordering = ['-id']
    #list_display =('title', 'order')

admin.site.register(TipoTelefono, TipoTelefonoAdmin)

class Cliente_telefonoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'numero', 'tipo_numero']
    search_fields = ('numero','cliente')
    ordering = ['cliente']

admin.site.register(Cliente_telefono, Cliente_telefonoAdmin)