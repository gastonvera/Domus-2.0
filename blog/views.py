from django.shortcuts import render
from django.views.generic import *


class Inicio(TemplateView):
    template_name = 'inicio.html'


class Propiedades(TemplateView):
    template_name = 'propiedades.html'


class Reserva(TemplateView):
    template_name = 'FormReserva.html'


class Contacto(TemplateView):
    template_name = 'contacto.html'


class Nosotros(TemplateView):
    template_name = 'nosotros.html'


class Detalle(TemplateView):
    template_name = 'caracteristica.html'
