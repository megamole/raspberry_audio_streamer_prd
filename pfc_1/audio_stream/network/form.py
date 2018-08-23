from django import forms
from .models import Wifi

class WifiForm (forms.ModelForm):

   # el parametro SSID lo paso directamente al objecto Wifi, no hace falta enviarlo en el formulario asi que lo hago no requerido
   # para que asi form.is_valid() no espere que se le pase

   SSID = forms.CharField(required=False)
   class Meta:
            model = Wifi
            fields = ['SSID','password']

          # le decimos a django que este campo es una clave
            widgets = {'password': forms.PasswordInput()}
            

   def __str__(self):
     return str(self.SSID)