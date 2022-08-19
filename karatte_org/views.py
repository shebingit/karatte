from atexit import register
from email import message
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


def Starz(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'Admin_profile.html')

def contact(request):
    return render(request,'contact.html')
    
@login_required(login_url="/Starz")
def load_admin_home(request):
    newss=news.objects.all()
    return render(request,'adminhome.html',{'newss':newss})


@login_required(login_url="/Starz")
def load_folder_create(request):
    folders=imagefolder.objects.all()
    return render(request,'folder.html',{'folders':folders})


@login_required(login_url="/Starz")
def load_updatefolder(request,folderl_id):
    folderl=imagefolder.objects.get(id=folderl_id)
    return render(request,'folderupdate.html',{'folderl':folderl})

@login_required(login_url="/Starz")
def load_affiliation(request):
    affili=affiliation.objects.get(id=2)
    return render(request,'affiliation_add.html',{'affili':affili})

def loadpdfimgs(request):
    pdfimgs=pdfimg.objects.all()
    return render(request,'pdfimg.html',{'pdfimgs':pdfimgs})

def loadmorecont(request,morec_id):
    con_id=contents.objects.get(id=morec_id)
    more=moreconts.objects.filter(con_id=morec_id)
    return render(request,'morecontent.html',{'more':more,'con_id':con_id})

def aboutmore(request,abm_id):
    con_id=contents.objects.get(id=abm_id)
    abtmore=moreconts.objects.filter(con_id=abm_id)
    return render(request,'morecontetuser.html',{'abtmore':abtmore,'con_id':con_id})

@login_required(login_url="/Starz")
def load_syllabus(request):
    pdfimgs=pdfimg.objects.all()
    return render(request,'syllabus.html',{'pdfimgs':pdfimgs})


def history(request):
    return render(request,'history1.html')

# carosel-----
@login_required(login_url="/Starz/")
def load_carousel(request):
    a=carousel.objects.all()
    return render(request,'carousel.html',{ 'al':a})

@login_required(login_url="/Starz")
def load_updatecarosel(request,upcarslid):
    carsl=carousel.objects.get(id=upcarslid)
    return render(request,'carsouelupdate.html',{'carsl':carsl})

@login_required(login_url="/Starz")
def load_assoupdate(request,assoup_id):
    asso=members.objects.get(id=assoup_id)
    return render(request,'associateupdate.html',{'asso':asso})

@login_required(login_url="/Starz")
def add_carousel_images(request):
    if request.method=='POST':
        title=request.POST['title']
        subtitle=request.POST['subtitle']
        carimage=request.FILES.get('carimgss')
        
        carousel.objects.create(
                title=title,subtitle=subtitle,carimage=carimage
                )
        return redirect('load_carousel')

@login_required(login_url="/Starz")
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

@login_required(login_url="/Starz")
def deletecarouselimg(request,carid_id):
    carimage=carousel.objects.get(id=carid_id)
    carimage.delete()
    return redirect('load_carousel')

# end carosel------


@login_required(login_url="/Starz")
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
                        newss=news.objects.all()
                        msg='Admin Succefully login'
                        return render(request,'adminhome.html',{'newss':newss,'msg':msg})
                        
                    else:
                        message='Invalid username or password'
                        return render(request,'login.html',{'message':message})
            except:
                message='Invalid username or password'
                return render(request,'login.html',{'message':message})                       
        else:
            #messages.info(request, 'Invalid username or password')
            message='Invalid username or password'
            return render(request,'login.html',{'message':message})
                   
    except:
       # messages.info(request, 'Invalid username or password')
        message='Invalid username or password'
        return render(request,'login.html',{'message':message})




#admin folder name update

@login_required(login_url="/Starz")
def update_folder(request,folderu_id):
    if request.method=="POST":
        folder=imagefolder.objects.get(id=folderu_id)
        folder.folder_name=request.POST.get('file')
        folder.save()
        folders=imagefolder.objects.all()
        return render(request,'folder.html',{'folders':folders,})
    else:
        return redirect('load_admin_home')

@login_required(login_url="/Starz")
def uploadvideo(request):
    if request.method=="POST":
        vi=request.POST['videofile']
        try:
            status=videos.objects.get(id=0)
        except videos.DoesNotExist:
            status=None

        if (status==None):
            vid=videos(video=vi)
            vid.save()
        else:
            vid=videos.objects.get(id=0)
            vid.video=request.POST.get('videofile')
            vid.save()

        
        messages="Video Saved Successfuly..."
        return render(request,'adminhome.html')

@login_required(login_url="/Starz")
def load_blackbelts(request):
    bths=blackbelt_holders.objects.all()
    associate=members.objects.all()
    return render(request,'blackbelt.html',{'bths':bths,'associate':associate})

@login_required(login_url="/Starz")
def load_addmember(request):
    return render(request,'addmember.html')

@login_required(login_url="/Starz")
def load_addimages(request):
    return render(request,'addimages.html')

@login_required(login_url="/Starz")
def load_associate(request):
    return render(request,'addmember.html')

@login_required(login_url="/Starz")
def loadadd_content(request):
    a=contents.objects.all()
    content=About.objects.all()
    return render(request,'content.html',{'al':a,'content':content})

@login_required(login_url="/Starz")
def load_history_add(request):
    history=HistoyrPdf.objects.all()
    return render(request,'history_add.html',{'history':history})

@login_required(login_url="/Starz") 
def add_content(request):
     if request.method=='POST':
        title=request.POST['conttitle']
        cont=request.POST['conts']
        contimage=request.FILES.get('contimg')
        
        contents.objects.create(
                con_title=title,con_content=cont,cont_img=contimage
                )
        return redirect('loadadd_content')


@login_required(login_url="/Starz")
def add_morecontent(request,admore_id):
     if request.method=='POST':
        cont=request.POST['moreconts']
        contimage=request.FILES.get('mcontimg')
        c_id=contents.objects.get(id=admore_id)
        moreconts.objects.create(con_id=c_id,
                more_cont=cont,more_img=contimage
                )
        return redirect('loadadd_content')

@login_required(login_url="/Starz")    
def morecontdelete(request,mcd_id):
    morecont=moreconts.objects.get(id=mcd_id)
    morecont.delete()
    return redirect('loadadd_content')

@login_required(login_url="/Starz")
def load_member(request):
    check_reg_member=check_register_members.objects.filter(check_status='0')
    reg_member=register_members.objects.all()
    return render(request,'show_member.html',{'reg_member':reg_member,'check_reg_member':check_reg_member})

def load_register(request):
    return render(request,'registration.html')

# admin folder create

@login_required(login_url="/Starz")
def create_folder(request):
    if request.method=="POST":
        fname=request.POST['file']

 #saving data

        folder=imagefolder(folder_name=fname,)

        folder.save()
        return redirect('load_folder_create')
    else:
        return redirect('load_admin_home')

@login_required(login_url="/Starz")
def deletefolder(request,fldd_id):
    folderdelete=imagefolder.objects.get(id=fldd_id)
    folderdelete.delete()
    return redirect(load_folder_create)

@login_required(login_url="/Starz")
def news_delete(request,news_id):
    newsd=news.objects.get(id=news_id)
    newsd.delete()
    return redirect('load_admin_home')

@login_required(login_url="/Starz")
def delete_syllabus(request,sydid):
    sylb=pdfimg.objects.get(id=sydid)
    sylb.delete()
    pdfimgs=pdfimg.objects.all()
    return render(request,'syllabus.html',{'pdfimgs':pdfimgs})


@login_required(login_url="/Starz")
def load_images(request,folimg_id):
    folder=imagefolder.objects.get(id=folimg_id)
    folder_images=images.objects.filter(folder_id=folimg_id)
    return render(request,'images.html',{'folder_images':folder_images,'folder':folder})

#adding images to a folder 
@login_required(login_url="/Starz")
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

@login_required(login_url="/Starz")
def uploadpdfimgs(request):
     if request.method=='POST':
        image=request.FILES.getlist('pdfimg')
        for imag in image:
            pdfimg.objects.create(
                more_img=imag)
        return redirect('load_admin_home')

@login_required(login_url="/Starz")
def uploadhistory(request):
    if request.method=='POST':
        image=request.FILES.getlist('historyimg')
        for imag in image:
            HistoyrPdf.objects.create(
                histry_img=imag)
        return redirect('load_history_add')

@login_required(login_url="/Starz")
def admin_events_image(request,evnt_id):
    events=news.objects.get(id=evnt_id)
    regf=regforms.objects.filter(env_id=evnt_id)
    evimg=eventimage.objects.filter(envimage_id=evnt_id)
    return render(request,'admin_event_imag.html',{'events':events,'regf':regf,'evimg':evimg})


@login_required(login_url="/Starz")
def regform(request,regform_id):
    if request.method=='POST': 
        fpdf=request.FILES.get('regfompdf')
        evnt_news=news.objects.get(id=regform_id)
        regf=regforms(regpdf=fpdf,env_id=evnt_news)
        regf.save()
        return redirect('load_admin_home')

@login_required(login_url="/Starz")
def eventimgupload(request,eventimg_id):
    if request.method=='POST': 
        impdf=request.FILES.get('evntimgpdf')
        evimags=request.FILES.get('evnt_img')
        evnt_news=news.objects.get(id=eventimg_id)
        regf=eventimage(envimgpdf=impdf,evnimg=evimags,envimage_id=evnt_news)
        regf.save()
        return redirect('load_admin_home')

@login_required(login_url="/Starz")
def evregform_delete(request,evformdelete_id):
    regform=regforms.objects.get(id=evformdelete_id)
    regform.delete()
    return redirect('load_admin_home')

@login_required(login_url="/Starz")
def news_eventimg_delete(request,evimg_delete_id):
    evimg=eventimage.objects.get(id=evimg_delete_id)
    evimg.delete()
    return redirect('load_admin_home')

@login_required(login_url="/Starz")
def deleteimg(request,img_id):
    image=images.objects.get(id=img_id)
    image.delete()
    return redirect('load_folder_create')

@login_required(login_url="/Starz")
def deletecontent(request,dcontent_id):
    cont=contents.objects.get(id=dcontent_id)
    morecon=moreconts.objects.filter(con_id=dcontent_id)
    morecon.delete()
    cont.delete()
    return redirect('loadadd_content')

# load home page

def load_home_page(request):
    folimgs=images.objects.all().order_by('id')[:6] 
    folders=imagefolder.objects.all()
    bgimg=blackbelt_holders.objects.all()
    vids=videos.objects.first()
    a=carousel.objects.all()[1:]
    firstca=carousel.objects.first()
    newss=news.objects.all()
    conts=About.objects.get(id=1)
    conts1=About.objects.all().order_by('id')[1:] 
    con1=contents.objects.all().order_by('id')[:2]
    message="Successfully Registered."
    return render(request,'index.html',{'bgimg':bgimg,'folders':folders,'vids':vids,'folimgs':folimgs,'al':a,'firstca':firstca,'newss':newss,'con1':con1,'conts1':conts1,'conts':conts})

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


@csrf_exempt
def add_assosiate(request):

    if request.method=="POST":
        name=request.POST['mname']
        desig=request.POST['mdesig']
        position=request.POST['mposition']
        img=request.FILES.get('mimg')
        


 #saving data
        member=members(mname=name,
                    mdesig=desig,
                    mposition=position,asso_image=img)

        member.save()
        return redirect('load_blackbelts')
    else:
        return JsonResponse('load_addmember')

@csrf_exempt
def register_member(request):
    if request.method=="POST":
        rg_name=request.POST['rname']
        rg_gender=request.POST['rg']
        rg_bloodg=request.POST['rbg']
        rg_dob=request.POST['rdb']
        rg_national=request.POST['rn']
        rg_occup=request.POST['ro']
        rg_qualific=request.POST['rq']
        rg_phon=request.POST['phno']
        rg_email=request.POST['mail']
        rg_doj=request.POST['rdj']
        rg_pgname=request.POST['pg']
        rg_pgoccu=request.POST['po']
        rg_address=request.POST['pa']
        rg_reson=request.POST['reson']
        rg_exp=request.POST['exp']
        rg_op=request.POST['ho']
        rg_img=request.FILES.get('imgs')


    #saving data
        register=check_register_members(check_reg_name=rg_name,
                         check_reg_gender=rg_gender,
                         check_reg_bloodg=rg_bloodg,
                         check_reg_dob=rg_dob,
                         check_reg_national=rg_national,
                         check_reg_occup=rg_occup,
                         check_reg_qualific=rg_qualific,
                         check_reg_phon=rg_phon,
                         check_reg_email=rg_email,
                         check_reg_doj=rg_doj,
                         check_reg_pgname=rg_pgname,
                         check_reg_pgoccu=rg_pgoccu,
                         check_reg_address=rg_address,
                         check_reg_reson=rg_reson,
                         check_reg_exp=rg_exp,
                         check_reg_op=rg_op,
                         check_reg_img=rg_img,check_status='0')
        register.save()
        message="SUCCESS"
        return render(request,'registration.html',{'message':message})
    else:
        return JsonResponse('load_home_page')
        

def check_reg_meberadd(request,check_addid):

    check_reg=check_register_members.objects.get(pk=check_addid)
    check_reg.check_status=str(1)
    check_reg.save()
    #saving data
    register=register_members(reg_name=check_reg.check_reg_name,
                         reg_gender=check_reg.check_reg_gender,
                         reg_bloodg=check_reg.check_reg_bloodg,
                         reg_dob=check_reg.check_reg_dob,
                         reg_national=check_reg.check_reg_national,
                         reg_occup=check_reg.check_reg_occup,
                         reg_qualific=check_reg.check_reg_qualific,
                         reg_phon=check_reg.check_reg_phon,
                         reg_email=check_reg.check_reg_email,
                         reg_doj=check_reg.check_reg_doj,
                         reg_pgname=check_reg.check_reg_pgname,
                         reg_pgoccu=check_reg.check_reg_pgoccu,
                         reg_address=check_reg.check_reg_address,
                         reg_reson=check_reg.check_reg_reson,
                         reg_exp=check_reg.check_reg_exp,
                         reg_op=check_reg.check_reg_op,
                         reg_img=check_reg.check_reg_img,)
    register.save()
    
    reg=register_members.objects.get(id=register.id)
    reg.register_id=str('JSA'+ str(reg.id)+'/KK/INDIA')
    reg.save()

    return redirect('load_member')

@login_required(login_url="/Starz")
def check_reg_delete(request,check_delete):
    checkdelete=check_register_members.objects.get(pk=check_delete)
    checkdelete.delete()
    return redirect('load_member')
                        
              
@login_required(login_url="/Starz")
def load_member_details(request,mdid):
    allmd=register_members.objects.get(id=mdid)
    return render(request,'reg_member_view.html',{'allmd':allmd})

   
@login_required(login_url="/Starz")
def reg_meberdelete(request,regdlid):
    reg=register_members.objects.get(id=regdlid)
    reg.delete()
    return redirect('load_member')
    

@csrf_exempt
@login_required(login_url="/Starz")
def add_news(request):

    if request.method=="POST":
        name=request.POST['news']
       
 #saving data
        newsadd=news(newstitle=name)

        newsadd.save()
        return redirect('load_admin_home')
    else:
        return JsonResponse('load_addmember')

# admin blackbelt holders update loaad data

@login_required(login_url="/Starz")
def load_bthupdate(request,bthu_id):
    bth=blackbelt_holders.objects.get(id=bthu_id)
    return render(request,'bthupdate.html',{'bth':bth})

#admin black belt member update
@login_required(login_url="/Starz")
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
        return redirect('load_admin_home')

@login_required(login_url="/Starz")
def updateassociate(request,upaso_id):
    if request.method=="POST":
        asso=members.objects.get(id=upaso_id)
        asso.mname=request.POST.get('name')
        asso.mdesig=request.POST.get('desig')
        asso.mposition=request.POST.get('position')
        asso.asso_image=request.FILES.get('img')
        asso.save()
        return redirect('load_blackbelts')
    else:
        return redirect('load_admin_home')




#admin black belt holder delete
@login_required(login_url="/Starz")
def bthdelete(request,bthd_id):
    bth=blackbelt_holders.objects.filter(id=bthd_id) 
    bth.delete()
    return redirect('load_blackbelts') 


#home page blackbelt view

def loadbackbelt_page(request):
    bths=blackbelt_holders.objects.all()
    asso=members.objects.all()
    return render(request,'blackbeltuser.html',{'bths':bths,'asso':asso})
    

#sending mail
@csrf_exempt
def sending_mail(request):
    if request.method == 'POST': 
        frommail = request.POST.get('smailid') 
        sendsub= request.POST.get('sub')
        msg=request.POST.get('msge')
        print(frommail)
        
        if frommail =='':
             message=" Please Fill email id"
        else:
            
            try:
                respons=send_mail(sendsub, msg,frommail,['jsaindia2022@gmail.com'])
                message=" THANK you for Contacting Us! Our Team will contact you Soon!..."
                return render(request,'sendmailout.html',{'message':message})
                
            except BadHeaderError:
                message="error!"
                return render(request,'sendmailout.html',{'message':message})
        return render(request,'sendmailout.html',{'message':message}) 


        
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

@login_required(login_url="/Starz")
def about_content(request):
    if request.method=="POST":
        ab_cont=request.POST['ab_content']
        conts=About(ab_contents=ab_cont)
        conts.save()
        mesg="successfully Saved."
        content=About.objects.all()
        a=contents.objects.all()
        return render(request,'content.html',{'al':a,'mesg':mesg,'content':content})

@login_required(login_url="/Starz")   
def about_delete(request,about_id):
    abcont=About.objects.get(id=about_id)
    abcont.delete()
    content=About.objects.all()
    a=contents.objects.all()
    return render(request,'content.html',{'al':a,'content':content})

@login_required(login_url="/Starz")
def about_content_update(request,abcontup_id):
    abcont=About.objects.get(id=abcontup_id)
    return render(request,'about_content_update.html',{'abcont':abcont})

@login_required(login_url="/Starz")
def about_content_save(request,abupdate_id):
    if request.method=="POST":
        abconts=About.objects.get(id=abupdate_id)
        abconts.ab_contents=request.POST.get('ab_content_save')
        abconts.save()
        content=About.objects.all()
        a=contents.objects.all()
        return render(request,'content.html',{'al':a,'content':content})

def Userevent_load(request):
    evtimgs=eventimage.objects.all()
    regformpdf=regforms.objects.all()
    return render(request,'Events.html',{'evtimgs':evtimgs,'regformpdf':regformpdf})


def associate_delete(request,ass_deleteid):
    asso=members.objects.filter(id=ass_deleteid)
    asso.delete()
    bths=blackbelt_holders.objects.all()
    associate=members.objects.all()
    return render(request,'blackbelt.html',{'bths':bths,'associate':associate})





    