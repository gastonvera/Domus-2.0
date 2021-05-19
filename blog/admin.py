from django.contrib.auth.models import User, Group
from django.contrib import admin
from .models import *


class CitasAdmin(admin.ModelAdmin):
    list_display = ("__str__", "nombre_apellido", "email", 'num_cliente', "propiedad", "agente", 'estado_cita')
    list_filter = ('estado_cita',)


class ClienteAdmin(admin.ModelAdmin):
    pass


class JefeAdministracionAdmin(admin.ModelAdmin):
    pass


class JefeComercializacionAdmin(admin.ModelAdmin):
    pass


class AgenteAdmin(admin.ModelAdmin):
    pass


class SecretariaAdmin(admin.ModelAdmin):
    pass


class PropiedadesAdmin(admin.ModelAdmin):
    list_display = ("__str__", "direccion", 'expensa', "precio", "tpo_propiedad", 'disponible')
    list_filter = ['disponible', 'tpo_propiedad']


class CajeraAdmin(admin.ModelAdmin):
    pass


class EmpleadoMarketingAdmin(admin.ModelAdmin):
    pass


def cerrar_caja(modeladmin, request, queryset):
    queryset.update(status='p')
cerrar_caja.allowed_permissions = ('delete',)


def generar_reporte(modeladmin, request, queryset):
    queryset.update(status='p')
generar_reporte.allowed_permissions = ('change','view')


class VentaAdmin(admin.ModelAdmin):
    list_display = ("__str__", "propiedad", "nya_cliente", 'estado_pago', 'fecha_creacion')
    list_filter = ['estado_pago', 'fecha_creacion']
    actions = [cerrar_caja, generar_reporte]


admin.site.register(Citas, CitasAdmin)
admin.site.register(Agente, AgenteAdmin)
admin.site.register(Secretaria, SecretariaAdmin)
admin.site.register(Cajera, SecretariaAdmin)
#admin.site.register(EmpleadoMarketing, EmpleadoMarketingAdmin)
admin.site.register(Propiedades, PropiedadesAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(JefeAdministracion, JefeAdministracionAdmin)
admin.site.register(JefeComercializacion, JefeComercializacionAdmin)
