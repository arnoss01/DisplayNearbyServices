from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
##from django.db.models import Model

# Create your models here.
class Service(models.Model):
    Nom_Service = models.TextField()
    Type_Service = models.CharField(max_length = 50)
    Longitude_Service = models.CharField(max_length = 50)
    Latitude_Service = models.CharField(max_length = 50) 
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="us")    
class Image(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images', null = True)
    Web_adresse_Img = models.TextField()

    