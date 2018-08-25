from django.db import models

# Create your models here.

class Config(models.Model):

    #valores posbiles de los atributos
	CHANNEL_CHOICES =(
    (1, "Mono"),
    (2, "Stereo"),
    ) 


	name=models.CharField(unique=True,max_length=10)

# INPUT

	device= models.CharField(max_length=6)
	sampleRate= models.PositiveSmallIntegerField()
	bitsPerSample= models.PositiveSmallIntegerField()
	channel= models.PositiveSmallIntegerField(choices=CHANNEL_CHOICES,default= 2)

# ICECAST2
	bitrateMode= models.CharField(max_length=3)
	format= models.CharField(max_length=10)
	quality= models.PositiveSmallIntegerField()
	channel_icecast= models.PositiveSmallIntegerField(choices=CHANNEL_CHOICES,default=2)
	bitrate= models.PositiveSmallIntegerField()
	server= models.URLField()
	port = models.PositiveSmallIntegerField()
	password= models.CharField(max_length=20)
	mountPoint= models.CharField(max_length=20)

   # def __str__(self):
		#return self.server