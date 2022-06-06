from xml.dom.minidom import Document
from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib import admin




urlpatterns =[ path('',views.load_home_page,name='load_home_page'),
               path('sending_mail',views.sending_mail,name='sending_mail'),
               path('load_affiliation_page',views.load_affiliation_page,name='load_affiliation_page'),
               path('loadbackbelt_page',views.loadbackbelt_page,name='loadbackbelt_page'),
               path('sort_img/<int:folimges>',views.sort_img,name='sort_img'),
               
            
               path('adminlogin',views.adminlogin,name='adminlogin'),
               path('changepassword',views.changepassword,name='changepassword'),

               path('login',views.login,name='login'),
               path('load_admin_home',views.load_admin_home,name='load_admin_home'),  # admin load home page
               path('load_folder_create',views.load_folder_create,name='load_folder_create'),
               path('load_blackbelts',views.load_blackbelts,name='load_blackbelts'),
               path('load_addmember',views.load_addmember,name='load_addmember'),
               path('add_blackbelt_holders',views.add_blackbelt_holders,name='add_blackbelt_holders'),
               path('load_bthupdate/<int:bthu_id>',views.load_bthupdate,name='load_bthupdate'),
               path('bthupdate/<int:bthud_id>',views.bthupdate,name='bthupdate'),
               path('bthdelete/<int:bthd_id>',views.bthdelete,name='bthdelete'),
               path('create_folder',views.create_folder,name='create_folder'),
               path('deletefolder/<int:fldd_id>',views.deletefolder,name='deletefolder'),
               path('load_updatefolder/<int:folderl_id>',views.load_updatefolder,name='load_updatefolder'),
               path('update_folder/<int:folderu_id>',views.update_folder,name='update_folder'),
               path('load_images/<int:folimg_id>',views.load_images,name='load_images'),
               path('load_addimages',views.load_addimages,name='load_addimages'),
               path('add_images_folder',views.add_images_folder,name='add_images_folder'),
               path('deleteimg/<int:img_id>',views.deleteimg,name='deleteimg'),
               path('load_affiliation',views.load_affiliation,name='load_affiliation'),
               path('uploadfile',views.uploadfile,name='uploadfile'),
               path('logout',views.logout,name='logout'),   

            ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

