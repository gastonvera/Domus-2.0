from django.contrib.auth.models import User
from django.db import models


TPO_CLIENTE = (
    ('CORPORATIVO', 'CORPORATIVO'),
    ('INDIVIDUO', 'INDIVIDUO'),
)


ESTADO_PAGO = (
    ('PAGADO', 'Pagado'),
    ('PENDIENTE', 'Pendiente'),
)


MEDIO_PAGO = (
    ('TRANSFERENCIA', 'Transferencia'),
    ('EFECTIVO', 'Efectivo'),
)


TPO_PROPIEDAD = (
    ('VENTA', 'Venta'),
    ('ALQUILER', 'Alquiler'),
)


FRENTE_CONTRAFRENTE = (
    ('FRENTE', 'Frente'),
    ('CONTRAFRENTE', 'Contrafrente'),
)

ORIENTACION = (
    ('ESTE', 'Este'),
    ('OESTE', 'Oeste'),
    ('NORTE', 'Norte'),
    ('SUR', 'Sur'),
)


class JefeAdministracion(models.Model):
    nombre = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre.username


class JefeComercializacion(models.Model):
    nombre = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre.username


class Cajera(models.Model):
    nombre = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre.username


class EmpleadoMarketing(models.Model):
    nombre = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre.username


class Agente(models.Model):
    nombre = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre.username


class Secretaria(models.Model):
    nombre = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre.username


class Propiedades(models.Model):
    pid = models.AutoField('PID', primary_key = True, unique = True, 
        help_text='Identificación de propiedad'
    )
    foto = models.ImageField('imagen de propiedad', blank = True, null = True)
    nombrep = models.CharField('Nombre', max_length = 50, blank = False, null = False)
    direccion = models.CharField('direccion', max_length = 100)
    superficie = models.CharField('Superficie', max_length=50, blank=False, 
        help_text='Superficie medida en m2'
    )
    piso = models.IntegerField('Piso')  
    dpto = models.CharField('Departamento', max_length=4)
    orientacion = models.CharField('orientacion', max_length = 5,
        choices = ORIENTACION
    )
    frente_contra = models.CharField('frente-contrafrente', max_length = 15,
        choices = FRENTE_CONTRAFRENTE
    )
    dormitorios = models.IntegerField('Dormitorios', blank=False)
    baños = models.IntegerField('Baños', blank=False)
    cocina = models.BooleanField('Cocina')
    comedor = models.BooleanField('Comedor')
    cochera = models.BooleanField('Cochera')  
    balcon = models.BooleanField('Balcon')
    observaciones = models.TextField('observaciones', max_length = 300,
        help_text='Datos adicionales para la propiedad',
        blank = True,
        null = True
    )
    expensa = models.DecimalField('Expensa', max_digits = 16, decimal_places = 2,
        help_text='Precio aproximado'
    )  
    precio = models.DecimalField('Precio', max_digits = 16, decimal_places = 2,
        help_text='Valor neto total de la propiedad/alquiler'
    )
    tpo_propiedad = models.CharField('Tipo de propiedad', max_length = 15,
        choices = TPO_PROPIEDAD
    )
    disponible = models.BooleanField('Disponible')

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"

    def __str__(self):
        nombre = str(self.nombrep)
        return nombre


class Citas(models.Model):
    identificacion = models.AutoField('ID Cita', primary_key = True, unique = True, 
        help_text='Identificación de propiedad'
    )
    nombre_apellido = models.CharField('Nombre cliente', max_length=100, blank=False)
    num_cliente = models.IntegerField('Cel./Tel.')
    email = models.EmailField('Email', blank = True, null = True)
    propiedad = models.ForeignKey(Propiedades, on_delete=models.CASCADE)
    fecha_cita = models.DateField('Fecha de cita', blank = True, null=True)
    hora_cita = models.TimeField('Hora de cita', blank=True, null=True)    
    agente = models.ForeignKey(Agente, on_delete = models.CASCADE, blank=True, null=True)
    estado_cita = models.BooleanField('Atendido/a', blank=True, null=True)


    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"


    def __str__(self):
        id = str(self.identificacion)
        return id


class Venta(models.Model):
    id_pay = models.AutoField('ID. Pago', primary_key = True, unique = True)
    propiedad = models.ForeignKey(Propiedades, on_delete = models.CASCADE)
    medio_pago = models.CharField('Medio de Pago', max_length = 25, choices = MEDIO_PAGO)
    nya_cliente = models.CharField('Nombre Cliente', max_length = 100, blank = False, null = False)
    dni_cli = models.IntegerField('DNI Cliente')
    estado_pago = models.CharField('Estado de Pago', max_length = 20, choices = ESTADO_PAGO)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now_add= True, editable=False)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"


    def __str__(self):
        id_pago = str(self.id_pay)
        return id_pago


class Cliente(models.Model):
    nombre = models.CharField('Nombre', max_length = 50, blank = False, null = False)
    apellido = models.CharField('apellido', max_length = 50, blank = False, null = False)
    domicilio = models.CharField('domicilio', max_length = 100, blank = False, null = False)
    dni = models.IntegerField('DNI Cliente')
    tpo_cliente = models.CharField('tipo de cliente', max_length = 20, choices = TPO_CLIENTE)


    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


    def __str__(self):
        return self.nombre