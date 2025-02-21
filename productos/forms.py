from django import forms
from .models import Producto

#formulario para cada class

class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'precio',
            'imagen'
        ]

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'ingresa el fakin nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-input'
                }
            )
        }

        labels = {
            'nombre': 'nombre del producto',
            'precio': 'precio del producto en MXN',
            'imagen': 'URL de la imágen'
        }

        error_messages = {

            'precio': {
                'required': 'el precio es requerido',
                'invalid': 'infresa un precio valido'
            }
        }