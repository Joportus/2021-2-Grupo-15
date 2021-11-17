from django import forms
from fwallet.models import User


class RegisterUser(forms.Form):
    """
    Clase que abstrae el formulario de resgistro de usuarios
    """
    usuario = forms.CharField(label="Nombre", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")    # max_length?
    email = forms.EmailField(label="Email")
    apodo = forms.CharField(label="Apodo")
    genero = forms.ChoiceField(choices=User.generos, label="Género")

