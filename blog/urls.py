from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    path('', (Inicio.as_view()), name='inicio'),
    path('propiedades/', (Propiedades.as_view()), name='propiedades'),
    path('reserva/', (Reserva.as_view()), name='form_reserva'),
    path('contacto/', (Contacto.as_view()), name='contacto'),
    path('nosotros/', (Nosotros.as_view()), name='nosotros'),
    path('detalle/', (Detalle.as_view()), name='detalle'),
]