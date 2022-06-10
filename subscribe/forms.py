# import form class from django
from django import forms
from django_countries.widgets import CountrySelectWidget

from catalog.models import emaillist

# create a ModelForm
class Subscribe(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = emaillist
		fields = "__all__"
	#	widgets = {'country': CountrySelectWidget()}
