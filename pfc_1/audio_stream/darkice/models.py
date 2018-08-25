from django.db import models

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
		('0.0' ,'0.0'),
		('0.1' ,'0.1'),
		('0.2' ,'0.2'),
		('0.3' ,'0.3'),
		('0.4' ,'0.4'),
		('0.5' ,'0.5'),
		('0.6' ,'0.6'),
		('0.7' ,'0.7'),
		('0.8' ,'0.8'),
        ('0.9' , '0.9'),
		('1.0' , '1.0'),
    )

	name=models.CharField(unique=True,max_length=10)

# INPUT

	device= models.CharField(max_length=6)
	sampleRate= models.PositiveSmallIntegerField(choices=SAMPLE_RATE_CHOICES,default=44100)
	bitsPerSample= models.PositiveSmallIntegerField(choices= BITS_PER_SAMPLE_CHOICES,default=16)
	channel= models.PositiveSmallIntegerField(choices=CHANNEL_CHOICES,default= 2)

# ICECAST2
	bitrateMode= models.CharField(choices=BITRATE__MODE_CHOICES,max_length=3)
	format= models.CharField(choices=FORMAT_CHOICES,default='mp3',max_length=3)
	quality= models.PositiveSmallIntegerField(choices=QUALITY_CHOICES,default=1.0)
	channel_icecast= models.PositiveSmallIntegerField(choices=CHANNEL_CHOICES,default=2)
	bitrate= models.PositiveSmallIntegerField(choices=BITRATE_CHOICES,default=128)
	server= models.URLField()
	port = models.PositiveSmallIntegerField(default=8000)
	password= models.CharField(max_length=20)
	mountPoint= models.CharField(max_length=20)

   # def __str__(self):
		#return self.server