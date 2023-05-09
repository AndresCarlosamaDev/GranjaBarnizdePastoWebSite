from django.db import models

# Create your models here.
class Products(models.Model):
    nombre_producto = models.CharField(max_length=50, null=False)
    peso = models.FloatField(null=False)
    material = models.CharField(max_length=100, null=False)
    detalles = models.CharField(max_length=150, null=False)
    descripcion = models.TextField(help_text='Ingresa una descripcion del producto', null=False)
    
    def __str__(self) -> str:
        producto_nombre = 'Producto: ' + self.nombre_producto
        return producto_nombre
    
class Imagenes_Producto(models.Model):
    imagen = models.ImageField(upload_to='galeria/product', null=True)
    producto = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='imagenes', null=False)