from django.db import models 
import datetime

# Create your models here.
class Post(models.Model):
    titulo=models.CharField(max_length=400)
    body=models.TextField()
    fecha_public=models.DateField(default=datetime.datetime.now())

class Coment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    contenido=models.CharField(max_length=50)