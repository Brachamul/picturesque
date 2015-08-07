from django import forms

from .models import *

from multiupload.fields import MultiFileField

class UploadForm(forms.ModelForm):
	class Meta :
		model = Medium
		fields = ['owner_tag']

	media = MultiFileField(min_num=1, max_num=80, max_file_size=1024*1024*50)
