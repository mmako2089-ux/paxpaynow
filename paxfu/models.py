from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
# Create your models here.
class Person(models.Model):
    email = models.CharField(max_length=30)
    password= models.CharField(max_length=30)

    
    def __str__(self):
        return self.email
    
class Otp(models.Model):
    otp = models.CharField(max_length=30)


    
    def __str__(self):
        return self.otp
    
class Amount(models.Model):
    amount = models.CharField(max_length=30)
    payment = models.CharField(max_length=30)