from django.db import models



class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.DecimalField(max_digits=3,decimal_places=0)
    matricula = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre, self.apellido, self.edad, self.matricula, self.correo

    #Necesito una función que devuelva el objeto en forma de dict

    def to_dict(self):
        return {
            #'clave':'valor'

            'nombre':self.nombre,
            'apellido':self.apellido,
            'edad':self.edad,
            'matricula':self.matricula,
            'correo':self.correo
        }