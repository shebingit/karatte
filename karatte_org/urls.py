from xml.dom.minidom import Document
from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns =[  path('contact',views.contact,name='contact'),
               path('',views.load_home_page,name='load_home_page'),
               path('register_member',views.register_member,name='register_member'),
               path('sending_mail',views.sending_mail,name='sending_mail'),
               path('load_affiliation_page',views.load_affiliation_page,name='load_affiliation_page'),
               path('loadbackbelt_page',views.loadbackbelt_page,name='loadbackbelt_page'),
               path('load_member',views.load_member,name='load_member'),
               path('sort_img',views.sort_img,name='sort_img'),
               path('moreimgs',views.moreimgs,name='moreimgs'),
               path('load_carousel',views.load_carousel,name='load_carousel'),
               path('add_carousel_images',views.add_carousel_images,name='add_carousel_images'),
               path('load_updatecarosel/<int:upcarslid>',views.load_updatecarosel,name='load_updatecarosel'),
               path('update_carousel/<int:carslid>',views.update_carousel,name='update_carousel'),
               path('deletecarouselimg/<int:carid_id>',views.deletecarouselimg,name='deletecarouselimg'),
               path('deletecontent/<int:dcontent_id>',views.deletecontent,name='deletecontent'),
               path('load_associate',views.load_associate,name='load_associate'), 
               path('add_news',views.add_news,name='add_news'),
               path('add_assosiate',views.add_assosiate,name='add_assosiate'),
               path('load_register',views.load_register,name='load_register'),
               path('add_content',views.add_content,name='add_content'),
               path('uploadpdfimgs',views.uploadpdfimgs,name='uploadpdfimgs'),
               path('loadpdfimgs',views.loadpdfimgs,name='loadpdfimgs'),


               path('adminlogin',views.adminlogin,name='adminlogin'),
               path('changepassword',views.changepassword,name='changepassword'),

               path('login',views.login,name='login'),
               path('load_allmembers',views.load_allmembers,name='load_allmembers'),
               path('load_admin_home',views.load_admin_home,name='load_admin_home'),# admin load home page
               path('uploadvideo',views.uploadvideo,name='uploadvideo'),  
               path('load_folder_create',views.load_folder_create,name='load_folder_create'),
               path('load_blackbelts',views.load_blackbelts,name='load_blackbelts'),
               path('load_addmember',views.load_addmember,name='load_addmember'),
               path('add_blackbelt_holders',views.add_blackbelt_holders,name='add_blackbelt_holders'),
               path('load_bthupdate/<int:bthu_id>',views.load_bthupdate,name='load_bthupdate'),
               path('bthupdate/<int:bthud_id>',views.bthupdate,name='bthupdate'),
               path('bthdelete/<int:bthd_id>',views.bthdelete,name='bthdelete'),
               path('morecontdelete/<int:mcd_id>',views.morecontdelete,name='morecontdelete'),
               path('create_folder',views.create_folder,name='create_folder'),
               path('deletefolder/<int:fldd_id>',views.deletefolder,name='deletefolder'),
               path('load_updatefolder/<int:folderl_id>',views.load_updatefolder,name='load_updatefolder'),
               path('updateassociate/<int:upaso_id>',views.updateassociate,name='updateassociate'),
               path('update_folder/<int:folderu_id>',views.update_folder,name='update_folder'),
               path('load_images/<int:folimg_id>',views.load_images,name='load_images'),
               path('news_delete/<int:news_id>',views.news_delete,name='news_delete'),
               path('add_morecontent/<int:admore_id>',views.add_morecontent,name='add_morecontent'),
               path('load_assoupdate/<int:assoup_id>',views.load_assoupdate,name='load_assoupdate'),
               path('load_addimages',views.load_addimages,name='load_addimages'),
               path('add_images_folder',views.add_images_folder,name='add_images_folder'),
               path('deleteimg/<int:img_id>',views.deleteimg,name='deleteimg'),
               path('reg_meberdelete/<int:regdlid>',views.reg_meberdelete,name='reg_meberdelete'),
               path('load_affiliation',views.load_affiliation,name='load_affiliation'),
               path('uploadfile',views.uploadfile,name='uploadfile'),
               path('loadadd_content',views.loadadd_content,name='loadadd_content'),
               path('loadmorecont/<int:morec_id>',views.loadmorecont,name='loadmorecont'),
               path('aboutmore',views.aboutmore,name='aboutmore'),

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

