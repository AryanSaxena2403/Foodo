from django.db import models

# Create your models here.
class help(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    concern=models.CharField(max_length=100)
