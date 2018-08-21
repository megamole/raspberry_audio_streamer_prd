from django import forms

from .models import Wifi

class WifiForm (forms.ModelForm):
   class Meta:
            model = Wifi
            fields = ('SSID','password',)

   def __str__(self):
     return str(self.SSID)