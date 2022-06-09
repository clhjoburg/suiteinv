from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.conf import settings
from django_countries.fields import CountryField
import datetime
import os
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.core.validators import FileExtensionValidator

# Create your models here.

User = settings.AUTH_USER_MODEL

class sound(models.Model):
    user = models.ForeignKey(User, default = 1, on_delete = models.CASCADE)
    sound_file = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    comments = models.TextField(max_length = 400, default = 'No comment')  
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
                ordering = ['-created_on']

    def get_absolute_url(self): # new
        return reverse('download-file')

class live(models.Model):
    user = models.ForeignKey(User, default = 1, on_delete = models.CASCADE)
    live_project_zip = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['zip'])])
    live_render = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    plug_in_1 = models.URLField(blank=True, max_length=200)
    plug_in_2 = models.URLField(blank=True, max_length=200)
    plug_in_3 = models.URLField(blank=True, max_length=200)
    plug_in_4 = models.URLField(blank=True, max_length=200)
    plug_in_5 = models.URLField(blank=True, max_length=200)
    comments = models.TextField(max_length = 400, default = 'No comment')  
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
                ordering = ['-created_on']

    def get_absolute_url(self): # new
        return reverse('live-download')

class livelarge(models.Model):
    file = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['zip'])])
    date_uploaded = models.DateTimeField(auto_now_add=True)            

class stem(models.Model):
    user = models.ForeignKey(User, default = 1, on_delete = models.CASCADE)
    track_1 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_1_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_2 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_2_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_3 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_3_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_4 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_4_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_5 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_5_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_6 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_6_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_7 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_7_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_8 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_8_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_9 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_9_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_10 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_10_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_11 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_11_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_12 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_12_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_13 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_13_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_14 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_14_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_15 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_15_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    track_16 = models.FileField(default='silence.mp3', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    track_16_pan = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    mixed_render = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])        
    comments = models.TextField(max_length = 400, default = 'No comment')  
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
                ordering = ['-created_on']

    def get_absolute_url(self): # new
        return reverse('stems-download')

class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length = 1000)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self): # new
        return reverse('contact-success')

class emaillist(models.Model):
    email = models.EmailField()
    country = CountryField(blank_label='(select country)', default = 'South Africa')  

    def get_absolute_url(self): # new
        return reverse('download-file')

class tourinput(models.Model):
    tour = models.TextField(default = 'No tour uploaded')        

class cameronbio(models.Model):
    bio = models.TextField(default = 'No bio uploaded')
    asideOne = models.TextField(default = 'No first aside uploaded')  
    asideTwo = models.TextField(default = 'No second aside uploaded')  

class cameronlinks(models.Model):
    links = models.TextField(default = 'No links uploaded')

class cameronworks(models.Model):
    works = models.TextField(default = 'No works uploaded')

class cameronnews(models.Model):
    news = models.TextField(default = 'No file uploaded')
    img1 =  models.ImageField(default = 'No file uploaded')
    img2 =  models.ImageField(default = 'No file uploaded')
    img3 =  models.ImageField(default = 'No file uploaded')
    img4 =  models.ImageField(default = 'No file uploaded')  
    img5 =  models.ImageField(default = 'No file uploaded')
    img6 =  models.ImageField(default = 'No file uploaded')  
    img7 =  models.ImageField(default = 'No file uploaded')
    img8 =  models.ImageField(default = 'No file uploaded')  
    img9 =  models.ImageField(default = 'No file uploaded')
    img10 =  models.ImageField(default = 'No file uploaded')  
    img11 =  models.ImageField(default = 'No file uploaded')
    img12 =  models.ImageField(default = 'No file uploaded')  
    img13 =  models.ImageField(default = 'No file uploaded')
    img14 =  models.ImageField(default = 'No file uploaded')  
    img15 =  models.ImageField(default = 'No file uploaded')
    img16 =  models.ImageField(default = 'No file uploaded')  
    img17 =  models.ImageField(default = 'No file uploaded')
    img18 =  models.ImageField(default = 'No file uploaded')  
    img19 =  models.ImageField(default = 'No file uploaded')
    img20 =  models.ImageField(default = 'No file uploaded')    

class cameroncontact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length = 1000)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self): # new
        return reverse('clh-contact-success')           

class cameronack(models.Model):
    acks = models.TextField(default = 'No acknowledgements uploaded')

class dkhhome(models.Model):
    homepage = models.TextField(default = 'No homepage uploaded')
    img1 =  models.ImageField(default = 'No file uploaded')
    img2 =  models.ImageField(default = 'No file uploaded')

class dkhnews(models.Model):
    news = models.TextField(default = 'No file uploaded')
    img1 =  models.ImageField(default = 'No file uploaded')
    img2 =  models.ImageField(default = 'No file uploaded')
    img3 =  models.ImageField(default = 'No file uploaded')
    img4 =  models.ImageField(default = 'No file uploaded')  
    img5 =  models.ImageField(default = 'No file uploaded')
    img6 =  models.ImageField(default = 'No file uploaded')  
    img7 =  models.ImageField(default = 'No file uploaded')
    img8 =  models.ImageField(default = 'No file uploaded')  
    img9 =  models.ImageField(default = 'No file uploaded')
    img10 =  models.ImageField(default = 'No file uploaded')  
    img11 =  models.ImageField(default = 'No file uploaded')
    img12 =  models.ImageField(default = 'No file uploaded')  
    img13 =  models.ImageField(default = 'No file uploaded')
    img14 =  models.ImageField(default = 'No file uploaded')  
    img15 =  models.ImageField(default = 'No file uploaded')
    img16 =  models.ImageField(default = 'No file uploaded')  
    img17 =  models.ImageField(default = 'No file uploaded')
    img18 =  models.ImageField(default = 'No file uploaded')  
    img19 =  models.ImageField(default = 'No file uploaded')
    img20 =  models.ImageField(default = 'No file uploaded')

class dkhlinks(models.Model):
    links = models.TextField(default = 'No links uploaded')

class dkhlisten(models.Model):
    listen = models.TextField(default = 'No audio uploaded')

class dkhabout(models.Model):
    about = models.TextField(default = 'No info uploaded')
    img1 =  models.ImageField(default = 'No file uploaded')
    img2 =  models.ImageField(default = 'No file uploaded')
    img3 =  models.ImageField(default = 'No file uploaded')
    img4 =  models.ImageField(default = 'No file uploaded')  
    img5 =  models.ImageField(default = 'No file uploaded')        

class dkhcontact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length = 1000)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self): # new
        return reverse('dkh-contact-success')                                                        
