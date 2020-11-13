from django import forms
from .models import Cliente


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
