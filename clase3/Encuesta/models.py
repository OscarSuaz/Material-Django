from django.db import models

class Pregunta(models.Model):
    pregunta=models.CharField(max_length=150)

    def __str__(self):
        return self.pregunta


class Opcion(models.Model):
    pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto=models.CharField(max_length=150)
    votos=models.IntegerField(default=0)

    def __str__(self):
        return self.texto +"  "+str(self.votos)