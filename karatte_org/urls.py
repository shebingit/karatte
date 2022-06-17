from xml.dom.minidom import Document
from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns =[ path('',views.load_home_page,name='load_home_page'),
               path('sending_mail',views.sending_mail,name='sending_mail'),
               path('load_affiliation_page',views.load_affiliation_page,name='load_affiliation_page'),
               path('loadbackbelt_page',views.loadbackbelt_page,name='loadbackbelt_page'),
               path('sort_img',views.sort_img,name='sort_img'),
               path('moreimgs',views.moreimgs,name='moreimgs'),
               path('load_carousel',views.load_carousel,name='load_carousel'),
               path('add_carousel_images',views.add_carousel_images,name='add_carousel_images'),
               path('load_updatecarosel/<int:upcarslid>',views.load_updatecarosel,name='load_updatecarosel'),
               path('update_carousel/<int:carslid>',views.update_carousel,name='update_carousel'),
               path('deletecarouselimg/<int:carid_id>',views.deletecarouselimg,name='deletecarouselimg'),
               
            
               path('adminlogin',views.adminlogin,name='adminlogin'),
               path('changepassword',views.changepassword,name='changepassword'),

               path('login',views.login,name='login'),
               path('load_admin_home',views.load_admin_home,name='load_admin_home'),# admin load home page
               path('uploadvideo',views.uploadvideo,name='uploadvideo'),  
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


               # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
            path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
            name='password_change_done'),

            path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
            name='password_change'),

            path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
            name='password_reset_done'),

            path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
            path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
            path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
            name='password_reset_complete'),


            ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

