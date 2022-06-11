from operator import truediv
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db import models
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


