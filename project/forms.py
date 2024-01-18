from django import forms
from .models import Upload, Output_Img

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['imgfile']

class Output_Img_Form(forms.ModelForm):
    class Meta:
        model = Output_Img
        fields = ['output_imgfile']