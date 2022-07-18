from asyncio.windows_events import NULL
from operator import truediv
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

class videos(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

# home background images

class hbgimg(models.Model):
    bg_image=models.ImageField(upload_to="image/bgimg", null=True)

#image folders

class imagefolder(models.Model):
    folder_name=models.CharField(max_length=25)
    
    def __str__(self):
        return self.folder_name


class affiliation(models.Model):
    affiliation_img=models.ImageField(upload_to="file",null=True)
    affiliation_name=models.ImageField(upload_to="file",null=True)



#images from the folder table

class images(models.Model):
    folder_id=models.ForeignKey(imagefolder,on_delete=models.CASCADE,null=True,blank=True)
    image_url=models.ImageField(upload_to="folderimages/", null=True)

    
class carousel(models.Model):
    carimage=models.ImageField(upload_to="carouselimages/", null=True)
    title=models.CharField(max_length=150)
    subtitle=models.CharField(max_length=150)


    def _str_(self):
        return self.title



# creating user signup details table

class blackbelt_holders(models.Model):

    bth_reg=models.CharField(max_length=25)
    bth_name=models.CharField(max_length=25)
    bth_desig=models.CharField(max_length=20)
    bth_image=models.ImageField(upload_to="image/blackbeltholder", null=True)

    def __str__(self):
        return self.bth_name

class news(models.Model):
    newstitle=models.CharField(max_length=150)
   


class members(models.Model):
    mname=models.CharField(max_length=30)
    mdesig=models.CharField(max_length=40)
    mposition=models.CharField(max_length=40)
    asso_image=models.ImageField(upload_to="image/blackbeltholder", null=True)

    def __str__(self):
        return self.mname

class register_members(models.Model):
    register_id=models.CharField(max_length=25)
    reg_name=models.CharField(max_length=25)
    reg_gender=models.CharField(max_length=10)
    reg_bloodg=models.CharField(max_length=10)
    reg_dob=models.CharField(max_length=20)
    reg_national=models.CharField(max_length=15)
    reg_occup=models.CharField(max_length=20)
    reg_qualific=models.CharField(max_length=20)
    reg_phon=models.CharField(max_length=15)
    reg_email=models.EmailField()
    reg_doj=models.CharField(max_length=20)
    reg_pgname=models.CharField(max_length=20)
    reg_pgoccu=models.CharField(max_length=20)
    reg_address=models.CharField(max_length=50)
    reg_reson=models.CharField(max_length=50)
    reg_exp=models.CharField(max_length=5)
    reg_op=models.CharField(max_length=5)
    reg_img=models.ImageField(upload_to="image/blackbeltholder")
    
    def save(self,*args,**kwargs):
        if self.register_id is None:
            self.register_id=str('JSA'+ str(self.id)+'/KK/INDIA')
        return super(register_members, self).save(*args,**kwargs)

class check_register_members(models.Model):
    check_reg_name=models.CharField(max_length=25)
    check_reg_gender=models.CharField(max_length=10)
    check_reg_bloodg=models.CharField(max_length=10)
    check_reg_dob=models.CharField(max_length=20)
    check_reg_national=models.CharField(max_length=15)
    check_reg_occup=models.CharField(max_length=20)
    check_reg_qualific=models.CharField(max_length=20)
    check_reg_phon=models.CharField(max_length=15)
    check_reg_email=models.EmailField()
    check_reg_doj=models.CharField(max_length=20)
    check_reg_pgname=models.CharField(max_length=20)
    check_reg_pgoccu=models.CharField(max_length=20)
    check_reg_address=models.CharField(max_length=50)
    check_reg_reson=models.CharField(max_length=50)
    check_reg_exp=models.CharField(max_length=5)
    check_reg_op=models.CharField(max_length=5)
    check_reg_img=models.ImageField(upload_to="image/regcheck")

class contents(models.Model):
    con_title=models.CharField(max_length=25)
    con_content=models.TextField()
    cont_img=models.ImageField(upload_to="image/blackbeltholder")
    def __str__(self):
        return self.con_title


class moreconts(models.Model):
    con_id=models.ForeignKey(contents,related_name='cont',on_delete=models.CASCADE,null=True,blank=True)
    more_cont=models.TextField()
    more_img=models.ImageField(upload_to="image/blackbeltholder")

class  pdfimg(models.Model):
    more_img=models.ImageField(upload_to="image/blackbeltholder")



