from tkinter import Widget
from django import forms
from .models import medico, inventario, conferencia, consulta


class medicosForm(forms.ModelForm):
    class Meta:
        model = medico
        fields = '__all__'
        widgets = {
            'nomMed': forms.TextInput(attrs={'class': 'validate'}),
            'aPat': forms.TextInput(attrs={'class': 'validate'}),
            'aMat': forms.TextInput(attrs={'class': 'validate'}),
            'edad': forms.NumberInput(attrs={'class': 'validate'}),
            'sexo': forms.TextInput(attrs={'class': 'validate'}),
        }


class inventarioForm(forms.ModelForm):
    class Meta:
        model = inventario
        fields = '__all__'
        widgets = {
            'nombreMat': forms.TextInput(attrs={'class': 'validate'}),
            'tipo': forms.TextInput(attrs={'class': 'validate'}),
            'cantidad': forms.NumberInput(attrs={'class': 'validate'}),
        }

class conferenciaForm(forms.ModelForm):
    class Meta:
        model = conferencia
        fields = '__all__'
        widgets = {
            'tema': forms.TextInput(attrs={'class': 'validate'}),
            'grupo': forms.TextInput(attrs={'class': 'validate'}),
            'fecha': forms.DateInput(attrs={'class': 'validate'}),
        }

class consultaForm(forms.ModelForm):
    class Meta:
        model = consulta
        fields = '__all__'
        widgets = {
            'fechaConsulta': forms.DateInput(attrs={'class': 'validate'}),
            'nombrePaci': forms.TextInput(attrs={'class': 'validate'}),
            'apPatPaci': forms.TextInput(attrs={'class': 'validate'}),
            'apMatPaci': forms.TextInput(attrs={'class': 'validate'}),
            'edadPaci': forms.NumberInput(attrs={'class': 'validate'}),
            'sexoPaci': forms.TextInput(attrs={'class': 'validate'}),
            'tipoPaci': forms.TextInput(attrs={'class': 'validate'}),
            'motivoCons': forms.Textarea(attrs={'rows': 10, 'cols': 40, 'class': 'materialize-textarea validate'}),
            'solucion': forms.Textarea(attrs={'rows': 10, 'cols': 40, 'class': 'materialize-textarea validate'}),
        }

