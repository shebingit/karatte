from atexit import register
from django.shortcuts import redirect, render
from urllib import request
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings
from django.core.mail import send_mail

#load admin home

def load_admin_home(request):
    return render(request,'adminhome.html')

def load_folder_create(request):
    return render(request,'folder.html')

def load_blackbelts(request):
    return render(request,'blackbelt.html')

def load_addmember(request):
    return render(request,'addmember.html')

# load home page

def load_home_page(request):
    return render(request,'index.html')

#sending mail

def sending_mail(request):
    if request.method == 'POST':
        subject = request.POST['subject'] 
        message = request.POST['message'] 
        recipient = request.POST['email'] 
        send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient])
        print(messages)
        messages.info(request,'sussessfull')
        
#load affiliation page

def load_affiliation_page(request):
    return render(request,'affiliation.html')