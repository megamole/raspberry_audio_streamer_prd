from django import forms

from .models import Config

class PostForm (forms.ModelForm):
   class Meta:
            model = Config
            fields = ('name','device', 'sampleRate','channel','bitsPerSample','bitrateMode','format','quality','channel_icecast','bitrate','server','port','password','mountPoint',)
            help_texts = {'name': "Nombre de la configuración",
            'device': "Dispositivo de grabación",
            'sampleRate': "Frecuencia de muestreo de la grabación",
            'bitsPerSample': "Bits por muestra",
            'channel':"Mono o estéreo",
            'bitrateMode': "Modo de la tasa de bits de la codificación",
            'format': "Formato del flujo enviado a Icecast",
            'quality':"Calidad de la codificación, 1.0 máxima calidad",
            'channel_icecast': "Número de canales de la salida, mono o estéreo",
            'bitrate': "Tasa de bits por segundo de la codificación",
            'server': "URL del servidor Icecast",
            'port': "Puerto del servidor Icecast",
            'password':"Clave para conectar al servidor Icecast",
            'mountPoint':"Punto de montaje en servidor Icecast",
            }
  

   def __str__(self):
     return str(self.name)