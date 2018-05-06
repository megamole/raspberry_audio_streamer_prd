from django.db import models

# Create your models here.

class Config(models.Model):
# INPUT
	device= models.CharField(max_length=6)
	sampleRate= models.PositiveSmallIntegerField()
	bitsPerSample= models.PositiveSmallIntegerField()
	channel= models.PositiveSmallIntegerField()

# ICECAST2
	bitrateMode= models.CharField(max_length=3)
	format1= models.CharField(max_length=10)
	quality= models.PositiveSmallIntegerField()
	channel= models.PositiveSmallIntegerField()
	bitrate= models.PositiveSmallIntegerField()
	server= models.URLField()
	port = models.PositiveSmallIntegerField()
	password= models.CharField(max_length=20)
	mountPoint= models.CharField(max_length=20)


