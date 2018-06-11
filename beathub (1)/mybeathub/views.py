from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from .models import *

def login(request):

    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render(request,'005.html') 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(('/accounts/login/'),3000)
    else:
        form = UserCreationForm()
    return render(request,'register.html',locals())


def contactus(request):
    content = ''
    if request.method == 'POST':
        content = request.POST.get('content')
        Contactus.objects.create(content=content)
    contactus = Contactus.objects.all()
    
    return render(request, 'contactus.html', {'contactus': contactus})
    



def index(request):
    return render(request,'index.html',locals())


def index001(request):
    return render(request,'001.html',locals())
def index0011(request):
    return render(request,'001-1.html',locals())
def index0012(request):
    return render(request,'001-2.html',locals())

def index002(request):
    return render(request,'002.html',locals())
def index0021(request):
    return render(request,'002-1.html',locals())
def index0022(request):
    return render(request,'002-2.html',locals())

def index003(request):
    return render(request,'003.html',locals())
def index0031(request):
    return render(request,'003-1.html',locals())
def index0032(request):
    return render(request,'003-2.html',locals())
def index004(request):
    return render(request,'004.html',locals())

def index005(request):
    return render(request,'005.html',locals())






def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')




def contactus2(request):
    return render(request,'contactus2.html',locals())