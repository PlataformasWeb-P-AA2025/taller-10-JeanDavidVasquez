from django.contrib import admin
from .models import Parroquia, BarrioCiudadela

class BarrioCiudadelaInline(admin.TabularInline):
    model = BarrioCiudadela
    extra = 1
    verbose_name = "Barrio o Ciudadela"
    verbose_name_plural = "Barrios o Ciudadelas"

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    list_filter = ('ubicacion', 'tipo')
    search_fields = ('nombre',)
    inlines = (BarrioCiudadelaInline,)

class BarrioCiudadelaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia')
    list_filter = ('numero_parques', 'parroquia')
    search_fields = ('nombre',)

admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(BarrioCiudadela, BarrioCiudadelaAdmin)