from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name



















# from rest_framework import serializers
# class Book(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     page = models.IntegerField()

# class BookSerializer(serializers.Serializer):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     page = models.IntegerField()