# import form class from django
from django import forms

# import GeeksModel from models.py
#from catalog.models import sound, stem, live, contact

from django.forms import FileInput

# create a ModelForm
'''
class Upload(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = sound
		widgets = {'document': FileInput(attrs={'accept': 'application/mp3,application/wav'})}
		exclude = ["user"]
		fields = ['sound_file', 'comments',]
		#fields = "__all__"

class StemUpload(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = stem
		widgets = {'document': FileInput(attrs={'accept': 'application/mp3,application/wav'})}
		exclude = ["user"]
		fields = ['mixed_render']
		#fields = "__all__"

class LiveUpload(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = live
		widgets = {'document': FileInput(attrs={'accept': 'application/mp3,application/wav,application/zip' })}
		exclude = ["user"]
		fields = ['live_render', 'comments',]		

class ContactUpload(forms.ModelForm):

	class Meta:
		model = contact
		fields = "__all__"
		
'''