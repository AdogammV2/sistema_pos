from django.db import models

# Create your models here.
class Provedor(models.Model):
    nombre = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13, unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Compras(models.Model):
    proveedor = models.ForeignKey(Provedor, on_delete=models.CASCADE, related_name='compras')
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='compras')
    estado = models.CharField(max_length=20, choices=[
        ('PENDIENTE', 'Pendiente'),
        ('RECIBIDO', 'Recibido'),
        ('CANCELADO', 'Cancelado'),
    ], default='PENDIENTE')
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Compra {self.id} - {self.proveedor.nombre} - {self.fecha_compra.strftime('%Y-%m-%d')}"
    
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE, related_name='compras')
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} - Compra {self.compra.id}"
