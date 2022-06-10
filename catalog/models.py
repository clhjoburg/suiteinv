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
