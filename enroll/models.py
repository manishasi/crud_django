from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100,unique=True)
