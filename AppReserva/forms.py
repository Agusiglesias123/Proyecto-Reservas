from django import forms


from .models import Reserva


class Solicitud(forms.ModelForm):
    class Meta:
        model = Reserva
        fields= [
            'nombre',
            'apellido',
            'telefono',
            'sector',
            'comensales',
            'fecha',
            'hora',

        ]

        labels= {
            'nombre' : 'Nombre',
            'apellid' : 'Apellido',
            'telefono' : 'Telefono',
            'sector' : 'Sector',
            'comensales' : 'Comensales',
            'fecha' : 'Fecha',
            'hora' : 'Hora',

        }
        widgets= {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellido' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'sector' : forms.TextInput(attrs={'class': 'form-control'}),
            'comensales' : forms.TextInput(attrs={'class': 'form-control'}),
            'fecha' : forms.DateInput(attrs={'type':'date'}),
            'hora' : forms.Select(attrs={'class': 'form-control'}),
            } 