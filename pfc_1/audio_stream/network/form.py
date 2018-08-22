from django import forms

from .models import Wifi

class WifiForm (forms.ModelForm):
   class Meta:
            model = Wifi
            fields = ['SSID','password']
            widgets = {
            # le decimos a django que este campo es una clave
            'password': forms.PasswordInput() 
        }


   def __str__(self):
     return str(self.SSID)