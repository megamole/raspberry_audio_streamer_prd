from django.shortcuts import render, HttpResponse,redirect
from django.http import Http404
from .form import PostForm
import os
import io
import re
import subprocess
import time
from django.contrib import messages
from darkice.models import Config

def detail(request,config_id):
    #configuration=Config.objects.order_by('-pk') [0]
    configuration=Config.objects.get(pk=config_id)
    return render(request, 'darkice/detailed_config.html',{'configuration': configuration,'pk' : config_id})




def list_configuration(request):
    configuration_list=Config.objects.all()
    return render(request, 'darkice/list_configuration.html',{'configuration_list': configuration_list})

def edit_configuration(request,config_id):
    new_config=Config.objects.get(pk=config_id)
    if request.method == 'POST':
        form=PostForm(request.POST,instance=new_config)

        if form.is_valid():
  
          new_config.device=form.cleaned_data['device']
          new_config.sampleRate=form.cleaned_data['sampleRate']
          new_config.bitsPerSample=form.cleaned_data['bitsPerSample']
          new_config.channel=form.cleaned_data['channel']
          new_config.bitrateMode=form.cleaned_data['bitrateMode']
          new_config.format=form.cleaned_data['format']
          new_config.quality=form.cleaned_data['quality']
          new_config.bitrate=form.cleaned_data['bitrate']
          new_config.channel_icecast=form.cleaned_data['channel_icecast']
          new_config.server=form.cleaned_data['server']
          new_config.port=form.cleaned_data['port']
          new_config.mountPoint=form.cleaned_data['mountPoint']
          new_config.save()  

    else:
          form = PostForm(instance=new_config)

    return render(request, 'darkice/config_edit.html', {'form': form})
    

def submit_configuration(request):
    #configuration=Config.objects.order_by('-pk') [0]
    configuration=Config()
    #render(request,'darkice/config_edit.html', {'form': form,})


    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            configuration=Config(
                device=form.cleaned_data['device'],
                sampleRate=form.cleaned_data['sampleRate'],
                bitsPerSample=form.cleaned_data['bitsPerSample'],
                channel=form.cleaned_data['channel'],
                bitrateMode=form.cleaned_data['bitrateMode'],
                format=form.cleaned_data['format'],
                quality=form.cleaned_data['quality'],
                bitrate=form.cleaned_data['bitrate'],
                channel_icecast=form.cleaned_data['channel_icecast'],
                server=form.cleaned_data['server'],
                port=form.cleaned_data['port'],
                mountPoint=form.cleaned_data['mountPoint'],
            )
            
            form.save()
            # do something.
    else:
        form = PostForm()
    return render(request, 'darkice/config_create.html', {'form': form,'configuration':configuration})


def darkice_process(request):
    return render(request, 'darkice/darkice_process.html')



def apply (request,config_id):
    # aplicamos la configuracion, para ello paremos el darkice y lo arrancamos con los nuevos valores
    #creamos el fichero de configuración y arrancamos el darkice con el nuevo fichero

    file_name="darkice_" + config_id + ".cfg"
    configuration=Config.objects.get(pk=config_id)
    file = open(file_name,'w')
    file.write('[general]\n'+'duration        = 0\n'+
                'bufferSecs      = 1\n'+'reconnect       = yes\n'+'\n[input]\n'+
                'device          = '+configuration.device+
                '\n'+'sampleRate      = '+str(configuration.sampleRate)+
                '\n'+'bitsPerSample   = '+str(configuration.bitsPerSample)+'\n'+
                'channel         = '+str(configuration.channel)+
                '\n\n[icecast2-0]\n'+
                'format          = '+configuration.format+'\n'+
                'bitrate         = '+str(configuration.bitrate)+'\n'+
                'bitrateMode     = '+configuration.bitrateMode+'\n'+
                'quality         = '+str(configuration.quality)+'\n'+
                'channel         = '+str(configuration.channel_icecast)+
                '\nlowpass         = 5000\n'+
                'server          = '+configuration.server+'\n'+
                'port            = '+str(configuration.port)+'\n'+
                'password        = '+configuration.password+'\n'+
                'mountPoint      = '+configuration.mountPoint+
                '\nname            = mystream'+ 
                '\ndescription     ='+  
                '\nurl             = localhost'+
                '\ngenre           = Scanner'+
                '\npublic          = yes'
            )
    file.close()

    command="darkice -c " + file_name
   
    os.system("pkill darkice")

    # arrancamos el darkice, si arranca correctamente no habrá mensaje de error

    p=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #for line in io.TextIOWrapper(p.stdout, encoding="utf-8"):
                  #messages.info(request,p.line)
    
    if subprocess.Popen("ps aux |grep -v grep| grep darkice",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]!=b'':

        return HttpResponse("La configuracion se ha aplicado correctamente")
    
    else:
        #se puede mejorar la presentacion del mensaje de error
        messages.info(request, 'Error al intentar arrancer DARKICE')
        messages.info(request,p.stdout.readlines()[-1])
        return redirect("/config_list/")






def delete_config (request,config_id):
    configuration=Config.objects.get(pk=config_id)
    #Config.objects.get(pk=config_id).delete()
    return render(request, 'darkice/config_delete.html', {'configuration':configuration})


def delete (request,config_id):
    #if request.method == 'POST':
    Config.objects.get(pk=config_id).delete()
    return redirect("/config_list/")






def start_darkice(request):
    if request.method == 'POST':
        os.system("darkice")
        #time.sleep(10)
        if subprocess.Popen("ps aux |grep -v grep| grep darkice2| awk '{print $2}'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]==b'':
        #if (os.system("ps aux |grep -v grep| grep darkice2| awk '{print $2}'"))=="":
            print ("proceso no arrancado correctamente")
        else:
             print ("proceso corriendo")
    #else:
    # form=PostForm() necesito aqui otro form no PostForm()
    return HttpResponse("Proceso arrancado")

def stop_darkice(request):

    if request.method == 'POST':
        #os.system("ps aux |grep -v grep| grep darkice| awk '{print $2}'|xargs kill")
        os.system("pkill darkice2")

    #else:
    #    form=PostForm()  necesito aqui otro form no PostForm()
    return HttpResponse("Proceso detenido")

