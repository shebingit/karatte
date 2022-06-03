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