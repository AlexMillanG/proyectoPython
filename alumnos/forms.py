from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:

        model = Alumno

        fields = [
            'nombre',
            'apellido',
            'edad',
            'matricula',
            'correo'
        ]

        widgets={
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-input',
                    'placeholder':'nombre del alumno'
                }
            )
        }

        labels={
            'nombre':'nombre del alumno'
        }
