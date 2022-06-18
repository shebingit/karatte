from atexit import register
import json
from django.http import BadHeaderError
from django.shortcuts import redirect, render
from urllib import request
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

#load admin home

fid=0
def adminlogin(request):
    return render(request,'login.html')

@login_required
def load_admin_home(request):
    return render(request,'adminhome.html')

def load_folder_create(request):
    folders=imagefolder.objects.all()
    return render(request,'folder.html',{'folders':folders})

def load_updatefolder(request,folderl_id):
    folderl=imagefolder.objects.get(id=folderl_id)
    return render(request,'folderupdate.html',{'folderl':folderl})

def load_affiliation(request):
    affili=affiliation.objects.get(id=2)
    return render(request,'affiliation_add.html',{'affili':affili})

# carosel-----

def load_carousel(request):
    a=carousel.objects.all()
    return render(request,'carousel.html',{ 'al':a})

def load_updatecarosel(request,upcarslid):
    carsl=carousel.objects.get(id=upcarslid)
    return render(request,'carsouelupdate.html',{'carsl':carsl})

def add_carousel_images(request):
    if request.method=='POST':
        title=request.POST['title']
        subtitle=request.POST['subtitle']
        carimage=request.FILES.get('carimgss')
        
        carousel.objects.create(
                title=title,subtitle=subtitle,carimage=carimage
                )
        return redirect('load_carousel')

def update_carousel(request,carslid):
    if request.method=="POST":
        carsl=carousel.objects.get(id=carslid)
        carsl.title=request.POST.get('uptitle')
        carsl.subtitle=request.POST.get('upsubtitle')
        carsl.carimage=request.FILES.get('upcarimgss')
        carsl.save()
        al=carousel.objects.all()
        return render(request,'carousel.html',{'al':al})
    else:
        return redirect('load_admin_home')

def deletecarouselimg(request,carid_id):
    carimage=carousel.objects.get(id=carid_id)
    carimage.delete()
    return redirect('load_carousel')

# end carosel------



def uploadfile(request):
    if request.method=="POST":
        fileimg=request.FILES.get('imgfile')
        file=request.FILES.get('file')
        aff=affiliation.objects.all()
        print(aff)
        if aff==0 :
            affiliation.objects.create(affiliation_name=file,affiliation_img=fileimg)
        else:
            affi=affiliation.objects.get(id=2)
            affi.affiliation_img=fileimg
            affi.affiliation_name=file
            affi.save() 
        return redirect('load_affiliation')

def login(request): 
    try:
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username, password=password)
                request.session["uid"] = user.id

                if user is not None:
                    auth.login(request, user)
                    if user.is_superuser==1:
                        return redirect ('load_admin_home')

            except:
                messages.info(request, 'Invalid username or password')
                return render(request, 'login.html')                        
        else:
            #messages.info(request, 'Invalid username or password')
            return render('login.html')        
    except:
       # messages.info(request, 'Invalid username or password')
        return render(request, 'login.html')




#admin folder name update

def update_folder(request,folderu_id):
    if request.method=="POST":
        folder=imagefolder.objects.get(id=folderu_id)
        folder.folder_name=request.POST.get('file')
        folder.save()
        folders=imagefolder.objects.all()
        return render(request,'folder.html',{'folders':folders,})
    else:
        return redirect('load_admin_home')

def uploadvideo(request):
    if request.method=="POST":
        vid=videos.objects.get(id=0)
        vid.video=request.POST.get('videofile')
        vid.save()
        messages="Video Saved Successfuly..."
        return render(request,'adminhome.html')

def load_blackbelts(request):
    bths=blackbelt_holders.objects.all()
    return render(request,'blackbelt.html',{'bths':bths})

def load_addmember(request):
    return render(request,'addmember.html')

def load_addimages(request):
    return render(request,'addimages.html')

# admin folder create
 
def create_folder(request):
    if request.method=="POST":
        fname=request.POST['file']

 #saving data

        folder=imagefolder(folder_name=fname,)

        folder.save()
        return redirect('load_folder_create')
    else:
        return redirect('load_admin_home')

def deletefolder(request,fldd_id):
    folderdelete=imagefolder.objects.get(id=fldd_id)
    folderdelete.delete()
    return redirect(load_folder_create)



def load_images(request,folimg_id):
    folder=imagefolder.objects.get(id=folimg_id)
    folder_images=images.objects.filter(folder_id=folimg_id)
    print(folder_images)
    return render(request,'images.html',{'folder_images':folder_images,'folder':folder})

#adding images to a folder 

def add_images_folder(request):
    if request.method=='POST':
        name=request.POST['name']
        image=request.FILES.getlist('imgs')
        folderid=imagefolder.objects.get(folder_name=name)
        for imag in image:
            images.objects.create(
                image_url=imag,
                folder_id=folderid)
        return redirect('load_images',folderid.id)

#admin delete single image

def deleteimg(request,img_id):
    image=images.objects.get(id=img_id)
    image.delete()
    return redirect('load_folder_create')



# load home page

def load_home_page(request):
    folimgs=images.objects.all().order_by('id')[:6] 
    folders=imagefolder.objects.all()
    bgimg=blackbelt_holders.objects.all()
    vids=videos.objects.first()
    a=carousel.objects.all()
    return render(request,'index.html',{'bgimg':bgimg,'folders':folders,'vids':vids,'folimgs':folimgs,'al':a})

@csrf_exempt
def sort_img(request):
    if request.method =="POST":
        folimges=request.POST.get('fid')
        if folimges=='0':
            folimgs=images.objects.all().order_by('id')[:6] 

        else:
            folimgs=images.objects.filter(folder_id=folimges).order_by('id')[:6] 
            
        return render(request,'sortedimgs.html',{'folimgs':folimgs})
    else:
        return HttpResponse({'value':0})
@csrf_exempt    
def moreimgs(request):
    if request.method =="POST":
        folimges=request.POST.get('fimgid')
        if folimges=='0':
            folimgs=images.objects.all() 
        else:
            folimgs=images.objects.filter(folder_id=folimges)
        return render(request,'moreimg.html',{'folimgs':folimgs})




# adding the black belt holders
@csrf_exempt
def add_blackbelt_holders(request):

    if request.method=="POST":
        reg=request.POST['regid']
        name=request.POST['name']
        desig=request.POST['desig']
        img=request.FILES.get('img')


 #saving data
        bth=blackbelt_holders(bth_reg=reg,
                          bth_name=name,
                          bth_desig=desig,
                          bth_image=img)

        bth.save()
        return redirect('load_blackbelts')
    else:
        return JsonResponse('load_addmember')
    
# admin blackbelt holders update loaad data

def load_bthupdate(request,bthu_id):
    bth=blackbelt_holders.objects.get(id=bthu_id)
    return render(request,'bthupdate.html',{'bth':bth})

#admin black belt member update

def bthupdate(request,bthud_id):
    if request.method=="POST":
        bth=blackbelt_holders.objects.get(id=bthud_id)
        bth.bth_reg=request.POST.get('regid')
        bth.bth_name=request.POST.get('name')
        bth.bth_desig=request.POST.get('desig')
        bth.bth_image=request.FILES.get('img')
        bth.save()
        return redirect('load_blackbelts')
    else:
        return redirect('load_addmember')



#admin black belt holder delete

def bthdelete(request,bthd_id):
    bth=blackbelt_holders.objects.filter(id=bthd_id) 
    bth.delete()
    return redirect('load_blackbelts') 


#home page blackbelt view

def loadbackbelt_page(request):
    bths=blackbelt_holders.objects.all()
    return render(request,'blackbeltuser.html',{'bths':bths})
    

#sending mail

def sending_mail(request):
    if request.method == 'POST': 
        recipient = request.POST['email'] 
        message=" THANKS YOU  for Contacting Us! Our Team will contact you Soon!..."
        sendsubject=" JKMO INDIA"
        try:
            respons=send_mail(sendsubject, message,settings.EMAIL_HOST_USER,[recipient])
            return render (request,'index.html',{'message':message})
            
        except BadHeaderError:
            return()


        
#load affiliation page

def load_affiliation_page(request):
    affili=affiliation.objects.get(id=2)
    return render(request,'affiliation.html',{'affili':affili})


def changepassword(request):
    return render(request,'changepassword.html')

def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('load_home_page')