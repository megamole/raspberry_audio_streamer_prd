from django import forms

from .models import Config

class PostForm (forms.ModelForm):
   class Meta:
            model = Config
            fields = ('name','device', 'sampleRate','bitsPerSample','channel','bitrateMode','format1','quality','bitrateMode','format1','quality','channel','bitrate','server','port','password','mountPoint',)

   def __str__(self):
     return str(self.name)