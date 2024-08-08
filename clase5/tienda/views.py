from django.shortcuts import render
from .models import *

# Create your views here.
def vista_categoria(request, clave):
    datos=Categoria.objects.get(clave=clave)
    return render(request, 'tienda/categoria.html',{"categoria":datos})



def vista_producto(request,clave,clave_prod):
    prod=Producto.objects.get(clave=clave_prod)
    return render(request, 'tienda/producto.html',{'producto':prod})