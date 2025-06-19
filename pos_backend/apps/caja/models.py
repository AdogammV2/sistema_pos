from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Caja(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    monto_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    esta_abierta = models.BooleanField(default=True)

    def __str__(self):
        return f"Caja de {self.usuario} - {self.fecha_apertura.strftime('%Y-%m-%d %H:%M:%S')}"
    
class MovimientoCaja(models.Model):
    TIPO_MOVIMIENTO = [
        ('INGRESO', 'Ingreso'),
        ('EGRESO', 'Egreso'),
        ('AJUSTE', 'Ajuste'),
        ('VENTA', 'Venta'),
    ]
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE, related_name='movimientos')
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.monto}"
    
class CorteCaja(models.Model):
    caja = models.OneToOneField(Caja, on_delete=models.CASCADE, related_name='corte')
    total_ventas = models.DecimalField(max_digits=10, decimal_places=2)
    total_ingresos = models.DecimalField(max_digits=10, decimal_places=2)
    total_egresos = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_corte = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Corte de Caja {self.caja}"
