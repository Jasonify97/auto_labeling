from django.db import models

class Upload(models.Model):
    imgfile = models.ImageField(upload_to='img/', blank=True, null=True)

class Output_Img(models.Model):
    output_imgfile = models.ImageField(upload_to='output/', blank=True, null=True)
