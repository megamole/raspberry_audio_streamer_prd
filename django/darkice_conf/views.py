from django.shortcuts import render

from django.http import HttpResponse

from .models import Config

def index(request):
    return render(request, 'darkice_conf/template.html')
# Create your views here.
