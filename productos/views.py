from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Imagenes_Producto

# Create your views here.
def index(request):
    productos = Products.objects.all()
    return render(request, 'index.html', {'productos': productos})

def tecnica(request):
    return render(request, 'tecnica.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def galeria(request):
    productos = Products.objects.all()
    return render(request, 'galeria.html', {'productos': productos})

def contacto(request):
    return render(request, 'contacto.html')

def prod_detalle(request, id):
    producto_ind = Products.objects.get(id=id)
    return render(request, 'prod_detalle.html',{'producto_ind': producto_ind})