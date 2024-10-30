from django.db import models


class login(models.Model): #tablas    
    user=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
# Create your models here.
