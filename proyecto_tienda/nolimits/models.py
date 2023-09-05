from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.TextField(max_length=100)
    precio = models.IntegerField(null=False)
    foto = models.ImageField(upload_to="imagen_bd/", null=True, blank=True)
    
    
