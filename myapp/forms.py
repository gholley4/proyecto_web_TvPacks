from django import forms
from .models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'rut', 'email', 'telefono',
                'region', 'fecha_nacimiento', 'tipo_pack')

        labels = {
            'nombre': 'Nombre',
            'rut': 'Rut',
            'email': 'Email',
            'telefono': 'Telefono',
            'region': 'Region',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'tipo_pack': 'Tipo Pack',

        }

        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.Select(choices="opciones_region", attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'tipo_pack': forms.Select(choices="opciones_tipo_pack", attrs={'class': 'form-control'}),
        }

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
            ]
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
        }

