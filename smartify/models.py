from django.db import models

class Smartify(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    date= models.DateField(blank=True, null=True) 
    time = models.TimeField(blank=True, null=True) 
    fimg = models.CharField(max_length=120, blank=True, null=True) 
    intro = models.TextField( blank=True, null=True)
    simg = models.CharField(max_length=120, blank=True, null=True)
    fpara = models.TextField( blank=True, null=True)
    timg = models.CharField(max_length=120, blank=True, null=True)
    spara = models.TextField( blank=True, null=True)
    oimg = models.CharField(max_length=120, blank=True, null=True)
    outro = models.TextField( blank=True, null=True)


    def __str__(self):
        return self.title