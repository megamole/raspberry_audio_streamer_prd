# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Wifi(models.Model):
# INPUT
  SSID= models.CharField(max_length=20,unique=True)
  password= models.CharField(max_length=20)

def __str__(self):
    return self.password