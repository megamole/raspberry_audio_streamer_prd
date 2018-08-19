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

def list_wifi(request):
        wifi_list=subprocess.run('nmcli -t  --fields SSID device wifi', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

        #por defecto la salida del comnado va carácter a carácter por lo que hay que extraer la información línea a línea manualmente

        return render(request, 'network/wifi_list.html',{'wifi_list':wifi_list.stdout.split('\n')})


def network_status(request):
    status=internet_on()
    if status:
        con_info = subprocess.check_output('nmcli con show -a', shell=True)
        stream=darkice.utils.is_connected("google.es")
    return render(request, 'network/network.html',{'status':status,'stream':stream,'con_info':con_info})()