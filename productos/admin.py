from django.contrib import admin
from .models import Products, Imagenes_Producto


# Register your models here.
class ImagenProductoAdmin(admin.TabularInline):
    model = Imagenes_Producto
    extra = 1

class ImageAdmin(admin.ModelAdmin):
   inlines = [ImagenProductoAdmin, ]
    
admin.site.register(Products, ImageAdmin);


