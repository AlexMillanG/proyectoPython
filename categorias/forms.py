from django import forms
from .models import Categoria

class categoryForm(forms.ModelForm):
    class Meta:
        model =Categoria

        fields=[
            'nombre',
            'imagen'
        ]

        widgets={
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-input',
                    'placeholder':'ingresa el nombre de la categoria'
                }
            )
        }

        labels ={
            'nombre':'nombre de la categoria',
            'imagen':'URL de la imagen'
        }