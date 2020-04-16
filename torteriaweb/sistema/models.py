from django.db import models


class Producto(models.Model):
    producto = models.CharField(max_length=255)
    descripcion = models.TextField(null=True,blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto