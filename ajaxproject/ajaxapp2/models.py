from django.db import models

# Create your models here.
class Userdata(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100) 


# Create your models here.
class Entry(models.Model):
    # if we want id then we have to create id here
    ID = models.CharField(max_length=10,primary_key=True)
    data1 = models.CharField(max_length=50)
    data2 = models.CharField(max_length=50)
    