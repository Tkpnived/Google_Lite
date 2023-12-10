from django.db import models

# Create your models here.
class cat(models.Model):
    Category=models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Link=models.CharField(max_length=100,null=True)
    Linkname = models.CharField(max_length=100, null=True)
    shotnot= models.CharField(max_length=100, null=True)
    Link2 = models.CharField(max_length=100, null=True)
    Linkname2 = models.CharField(max_length=100, null=True)
    shotnot2 = models.CharField(max_length=100, null=True)
    Link3 = models.CharField(max_length=100, null=True)
    Linkname3 = models.CharField(max_length=100, null=True)
    shotnot3 = models.CharField(max_length=100, null=True)
    Details = models.CharField(max_length=100)
    Image = models.ImageField(null=True)
    Image2 = models.ImageField(null=True)
    Image3 = models.ImageField(null=True)
    Image4 = models.ImageField(null=True)
    Image5 = models.ImageField(null=True)
    Image6 = models.ImageField(null=True)
