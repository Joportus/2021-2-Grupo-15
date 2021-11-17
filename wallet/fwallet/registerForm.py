from django import forms
from fwallet.models import RegistroDinero


class MoneyForm(forms.ModelForm):
    class Meta:
        model = RegistroDinero
        fields = ['monto', 'tipo', 'nombre', 'fecha', 'clase', 'descripcion']
        widgets = {'fecha': forms.DateInput(attrs={'type': 'date'}), 'descripcion':forms.Textarea()}



