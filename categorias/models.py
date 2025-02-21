from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre, self.imagen

    #Necesito una función que devuelva el objeto en forma de dict
    def to_dict(self):
        return {
            #'clave':'valor'

            'nombre':self.nombre,
            'imagen':self.imagen
        }