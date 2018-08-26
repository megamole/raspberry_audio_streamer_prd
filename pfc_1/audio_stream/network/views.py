# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import subprocess
from django.http import Http404,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from urllib.request import urlopen
import darkice.utils
from network.models import Wifi,__str__
from network.form import WifiForm




def index (request):
        return render(request, 'network/index.html')









def internet_on():  #igual deberia crear libreria o app network para estas cosas
   try:
        response = urlopen('https://www.google.es/', timeout=10)
        return True
   except: 
        return False

def list_wifi(request):
        wifi_list=subprocess.run('nmcli -t  --fields SSID device wifi', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

        #por defecto la salida del comnado va carácter a carácter por lo que hay que extraer la información línea a línea manualmente

        # creando una lista de las WIFI disponibles que ya tenemos en la DB y otra con las que no
        wifi_list_on_db =[]
        wifi_list_not_on_db=[]

        for wifi_network in wifi_list.stdout.split('\n'):
           if Wifi.objects.filter(SSID=wifi_network).exists():
               wifi_list_on_db.append(wifi_network)
           else: 
               wifi_list_not_on_db.append(wifi_network)
        
        return render(request, 'network/wifi_list.html',{'wifi_list_on_db': wifi_list_on_db,'wifi_list_not_on_db': wifi_list_not_on_db})


def network_status(request):
    status=internet_on()

    active_connections=int(subprocess.check_output('nmcli con show -a|wc -l', shell=True).decode().split()[0])-1

    if status:
        i=0
        con_info=[]
        while i<active_connections:
             #con_info = subprocess.check_output('nmcli con show -a', shell=True).decode().split('\n')[i++]
             con_info.append(subprocess.check_output('nmcli con show -a', shell=True).decode().split('\n')[i+1])
             i += 1


       #El nombre de la conexión también se obtiene con ubprocess.Popen("nmcli con show -a", shell=True, stdout=subprocess.PIPE).communicate()[0].decode().split()[4]
             stream=darkice.utils.is_connected("google.es")
    return render(request, 'network/network.html',{'status':status,'stream':stream,'con_info':con_info,'active_connections':active_connections})


def existing_wifi(request, Wifi_SSID):
     if Wifi.objects.filter(SSID="hola").exists():
       print("hola")
       #connect_wifi(wifi.SSID,wifi.password)
     else:
       # submit_wifi_details(request)
       print ("buuh")






def connect_wifi(request,Wifi_SSID):

 wifi=Wifi.objects.get(SSID=Wifi_SSID)
 cmd = "nmcli d wifi connect " + wifi.SSID + " password " + wifi.password
 output=subprocess.check_output(cmd,shell=True)

 if b'failed:' in output.split():
    wifi.delete()
    return redirect('/network/wifi') 
 else:
    return HttpResponse ("Conectado a " + Wifi_SSID)



def submit_wifi_details(request,Wifi_SSID):
    new_wifi=Wifi()

    if request.method == "POST":
        form= WifiForm(request.POST) 
        if form.is_valid(): 

          new_wifi.password=form.cleaned_data['password']
          new_wifi.SSID=Wifi_SSID
          new_wifi.save()
          connect_wifi(request,Wifi_SSID)
          return redirect('/network/status') 


        else: raise Http404 
    
    else:
        form = WifiForm()
    
    return render(request, 'network/connect_wifi.html', {'form': form,'wifi_SSID':Wifi_SSID})