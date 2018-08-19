# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import subprocess
from django.shortcuts import render
from urllib.request import urlopen
import darkice.utils


def internet_on():  #igual deberia crear libreria o app network para estas cosas
   try:
        response = urlopen('https://www.google.es/', timeout=10)
        return True
   except: 
        return False

def network_status(request):
    status=internet_on()
    if status:
        con_info = subprocess.check_output('nmcli con show -a', shell=True)
        stream=darkice.utils.is_connected("google.es")
    return render(request, 'network/network.html',{'status':status,'stream':stream,'con_info':con_info})