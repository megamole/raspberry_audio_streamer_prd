from django.shortcuts import render, HttpResponse
from django.http import Http404
from .form import PostForm
import os
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
          new_config.format1=form.cleaned_data['format1']
          new_config.quality=form.cleaned_data['quality']
          new_config.bitrate=form.cleaned_data['bitrate']
          new_config.server=form.cleaned_data['server']
          new_config.port=form.cleaned_data['port']
          new_config.mountPoint=form.cleaned_data['mountPoint']
          new_config.save()  
    else:
          form = PostForm(instance=new_config)

    return render(request, 'darkice/config_edit.html', {'form': form})
    

def submit_configuration(request):
    file = open('config.txt','w')
    #configuration=Config.objects.order_by('-pk') [0]
    configuration=Config()
    #form=PostForm(instance=Config.objects.last())
    render(request,'darkice/config_edit.html', {'form': form,})


    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print("here i am")
            configuration=Config(
                device=form.cleaned_data['device'],
                sampleRate=form.cleaned_data['sampleRate'],
                bitsPerSample=form.cleaned_data['bitsPerSample'],
                channel=form.cleaned_data['channel'],
                bitrateMode=form.cleaned_data['bitrateMode'],
                format1=form.cleaned_data['format1'],
                quality=form.cleaned_data['quality'],
                bitrate=form.cleaned_data['bitrate'],
                server=form.cleaned_data['server'],
                port=form.cleaned_data['port'],
                mountPoint=form.cleaned_data['mountPoint'],
            )
            file.write('[general]\n'+'duration        = 0\n'+
                'bufferSecs      = 1\n'+'reconnect       = yes\n'+'\n[input]\n'+
                'device          = '+configuration.device+
                '\n'+'sampleRate      = '+str(configuration.sampleRate)+
                '\n'+'bitsPerSample   = '+str(configuration.bitsPerSample)+'\n'+
                'channel         = '+str(configuration.channel)+
                '\n\n[icecast2-0]\n'+
                'format          = '+configuration.format1+'\n'+
                'bitrate         = '+str(configuration.bitrate)+'\n'+
                'bitrateMode     = '+configuration.bitrateMode+'\n'+
                'quality         = '+str(configuration.quality)+'\n'+
                'channel         = '+str(configuration.channel)+
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
            form.save()
            file.close()
            # do something.
    else:
        form = PostForm()
    return render(request, 'darkice/config_edit.html', {'form': form,'configuration':configuration})


def darkice_process(request):
    return render(request, 'darkice/darkice_process.html')


def start_darkice(request):
    if request.method == 'POST':
        os.system("darkice")
        if (os.system("ps aux |grep -v grep| grep darkice2| awk '{print $2}'"))=="":
            print ("no hay proceso")
        else:
             print ("proceso corriendo")
    #else:
    # form=PostForm() necesito aqui otro form no PostForm()
    return HttpResponse("Proceso arrancado")

def stop_darkice(request):

    if request.method == 'POST':
        os.system("ps aux |grep -v grep| grep tail| awk '{print $2}'|xargs kill")
    #else:
    #    form=PostForm()  necesito aqui otro form no PostForm()
    return HttpResponse("Proceso detenido")

