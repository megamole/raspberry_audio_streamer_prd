from django import forms

from .models import Config

class PostForm (forms.ModelForm):
   class Meta:
            model = Config
            fields = ('name','device', 'sampleRate','channel','bitsPerSample','bitrateMode','format','bitrateMode','quality','channel_icecast','bitrate','server','port','password','mountPoint',)

   def __str__(self):
     return str(self.name)