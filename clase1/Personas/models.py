from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nac=models.DateField()

    def verificacion_nombre(self):
        if self.nombre=="Oscar":
            return "Eres el titular"
        else:
            return "Tu no eres Oscar"
        
    def save(self, *args, **kwargs):
        print("Estas intentando guardar algo")
        super().save(*args,**kwargs)


class Trabajador(models.Model):
    rfc= models.CharField(max_length=50)
    edad=models.IntegerField()

    def yoTrabajo(self):
        pass

    class Meta:
        abstract=True


class Enfermero(Trabajador):
    turno=models.CharField(max_length=50)
    hospital=models.CharField(max_length=50)

    def yoTrabajo(self):
        print("Trabajo como enfermero")


    def save(self,*args,**kwargs):
        self.yoTrabajo()
        super().save(*args,**kwargs)


class Trabajo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions=(
            ("ver_trabajo", "Puede ver los trabajos"),
            ("Encontrar trabajo", "Puede encontrar trabajo")
        )


