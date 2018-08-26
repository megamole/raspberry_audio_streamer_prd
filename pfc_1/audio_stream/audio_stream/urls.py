"""audio_stream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from darkice.views import detail,submit_configuration,list_configuration,edit_configuration,darkice_process,stop_darkice,start_darkice,apply,delete,delete_config
from network.views import network_status,list_wifi,submit_wifi_details,connect_wifi

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^config/$', index, name='index'),
    #url(r'^config/<int:config_id>/', detail, name='detail'),
    url(r'^config/(\d+)/$', detail, name='detail'),
    url(r'^config/delete/(\d+)$', delete, name='delete'),
    url(r'^config/edit/(\d+)/$', edit_configuration, name='edit_configuration'),
    #url(r'^config/edit/(?P<name>\w+)$', edit_configuration, name='edit_configuration'),
    url(r'^config_list/$', list_configuration, name='list_configuration'),
    url(r'^config/new/$', submit_configuration, name='submit_configuration'),
    url(r'^config_list/apply/(\d+)$', apply, name='apply'),
    url(r'^config/delete_config/(\d+)$', delete_config, name='delete_config'),
    url(r'^darkice/$', darkice_process, name='darkice_process'),
    url(r'^darkice/stop$', stop_darkice, name='stop_darkice'),
    url(r'^darkice/start$', start_darkice, name='start_darkice'),
    url(r'^network/status$', network_status, name='network_status'),    
    url(r'^network/wifi$',list_wifi , name='list_wifi'),
    url(r'^network/connect/(?P<Wifi_SSID>[\w\-]+.+.)$',submit_wifi_details,name='submit_wifi_details'),
    url(r'^network/connecting/(?P<Wifi_SSID>\w+)$',connect_wifi,name='connect_wifi'),



]
