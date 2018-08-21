# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import subprocess
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from urllib.request import urlopen
import darkice.utils
from network.models import Wifi,__str__
from network.form import WifiForm


def internet_on():  #igual deberia crear libreria o app network para estas cosas
   try:
        response = urlopen('https://www.google.es/', timeout=10)
        return True
   except: 
        return False

def list_wifi(request):
        wifi_list=subprocess.run('nmcli -t  --fields SSID device wifi', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

        #por defecto la salida del comnado va carácter a carácter por lo que hay que extraer la información línea a línea manualmente
        wi=Wifi.objects.filter(SSID=wifi_list.stdout.split('\n')[0])
        print(wi[0].password)

        return render(request, 'network/wifi_list.html',{'wifi_list':wifi_list.stdout.split('\n')})


def network_status(request):
    status=internet_on()
    if status:
        con_info = subprocess.check_output('nmcli con show -a', shell=True)
        stream=darkice.utils.is_connected("google.es")
    return render(request, 'network/network.html',{'status':status,'stream':stream,'con_info':con_info})()



def existing_wifi(request, Wifi_SSID):
     if Wifi.objects.filter(SSID="hola").exists():
       print("hola")
       #connect_wifi(wifi.SSID,wifi.password)
     else:
        submit_wifi_details(request)



def submit_wifi_details(request):
    if request.method == 'POST':
        form = WifiForm(request.POST)
        if form.is_valid():
            new_wifi=Wifi(
                SSID=form.cleaned_data['SSID'],
                password=form.cleaned_data['password'],
            )
        new_wifi.save()  
    else:
          form = WifiForm()

    return render(request, 'network/connect_wifi.html', {'form': form})