from xml.dom.minidom import Document
from django.views import *
from django.urls import  path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib import admin




urlpatterns =[ path('',views.load_home_page,name='load_home_page'),
               path('sending_mail',views.sending_mail,name='sending_mail'),
               path('load_affiliation_page',views.load_affiliation_page,name='load_affiliation_page'),


     ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

