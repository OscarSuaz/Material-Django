from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    clave=models.SlugField()

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    clave=models.SlugField()

    def __str__(self) -> str:
        return self.nombre