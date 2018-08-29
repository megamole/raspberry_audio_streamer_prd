from django.db import models
import os

# Create your models here.

class Config(models.Model):

    #valores posbiles de los atributos
	CHANNEL_CHOICES =(
    (1, "Mono"),
    (2, "Stereo"),
    ) 

	BITS_PER_SAMPLE_CHOICES =(
		(16, "16 (for mono feeds)"),
		(32,"32 (for stereo feeds)"),
	)

	BITRATE_CHOICES=(
		(96,"96Kbps"),
		(128,"128Kbps"),
		(160,"160Kbps"),
		(192,"192Kbps"),
		(320,"96Kbps"),
    )

	SAMPLE_RATE_CHOICES =(
		(11025 , "11025 Hz"),
        (22050 , "22050 Hz"),
		(44100 , "44100 Hz"),
		(48000 , "48000 Hz"),
    )

	FORMAT_CHOICES =(
		('vorbis' ,'vorbis'),
		('mp3' ,'mp3'),
		('mp2','mp2'),
		('aac' ,'aac'),
		('aacp' ,'aacp'),
	)

	BITRATE__MODE_CHOICES =(
		('cbr' ,'cbr'),
        ('abr' ,'abr'),
        ('vbr',"vbr"),
	)

	QUALITY_CHOICES= (
		(0.0 ,'0.0'),
		(0.1 ,'0.1'),
		(0.2 ,'0.2'),
		(0.3 ,'0.3'),
		(0.4 ,'0.4'),
		(0.5 ,'0.5'),
		(0.6 ,'0.6'),
		(0.7 ,'0.7'),
		(0.8 ,'0.8'),
        (0.9 , '0.9'),
		(1.0, '1.0'),
    )

	os.system("/home/chema/.WORK/pfc_1/audio_stream/dispositivos.sh")

	name=models.CharField(unique=True,max_length=10)

# INPUT

	device= models.CharField(max_length=6,help_text="Dispositivo de grabación")
	sampleRate= models.PositiveSmallIntegerField(choices=SAMPLE_RATE_CHOICES,default=44100,help_text="Frecuencia de muestreo de la grabación")
	bitsPerSample= models.PositiveSmallIntegerField(choices= BITS_PER_SAMPLE_CHOICES,default=16,help_text="Bits por muestra")
	channel= models.PositiveSmallIntegerField(choices=CHANNEL_CHOICES,default= 2,help_text="Mono o estéreo")

# ICECAST2
	bitrateMode= models.CharField(choices=BITRATE__MODE_CHOICES,max_length=3,help_text="Modo de la tasa de bits de la codificación")
	format= models.CharField(choices=FORMAT_CHOICES,default='mp3',max_length=3,help_text="Formato del flujo enviado a Icecast")
	quality= models.DecimalField(choices=QUALITY_CHOICES,default=1.0,max_digits=2,decimal_places=1,help_text="Calidad de la codificación, 1.0 máxima calidad")
	channel_icecast= models.PositiveSmallIntegerField(choices=CHANNEL_CHOICES,default=2,help_text="Número de canales de la salida, mono o estéreo")
	bitrate= models.PositiveSmallIntegerField(choices=BITRATE_CHOICES,default=128,help_text="Tasa de bits por segundo de la codificación")
	server= models.CharField(help_text="URL o IP del servidor Icecast, sin http / https",max_length=20)
	port = models.PositiveSmallIntegerField(default=8000,help_text="Puerto del servidor Icecast")
	password= models.CharField(max_length=20,help_text="Clave para conectar al servidor Icecast")
	mountPoint= models.CharField(max_length=20,help_text="Punto de montaje en servidor Icecast")

	def __str__(self):
		return self.name


	