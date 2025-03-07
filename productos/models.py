from django.db import models
from django.db.models import CharField
from categorias.models import Categoria



# Create your models here.

class DetallesProducto(models.Model):
    descripcion = models.CharField(max_length=300)
    fecha_cad = models.DateField()




class Proveedor(models.Model):
    nombre = CharField(max_length=100)
    contacto = CharField(max_length=200)





class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()


    #primer parametro es el modelo a relacionar y despues la estrategia de borrado
    detalles_producto = models.OneToOneField(DetallesProducto, on_delete=models.CASCADE)  # Se quitó el paréntesis extra en CASCADE

    proveedor = models.ManyToManyField(Proveedor)


    categoria = models.ForeignKey(Categoria, null=True,blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre, self.precio, self.imagen

    #Necesito una función que devuelva el objeto en forma de dict

    def to_dict(self):
        return {
            #'clave':'valor'

            'nombre':self.nombre,
            'precio':float(self.precio),
            'imagen':self.imagen
        }

