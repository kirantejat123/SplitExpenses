from django.db import models

# Create your models here.
class signInDetails(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30,primary_key=True)
    password=models.CharField(max_length=40)
class group(models.Model):
    groupName=models.CharField(max_length=50,primary_key=True)
    you=models.CharField(max_length=50)
    friend1=models.CharField(max_length=40)
    friend2=models.CharField(max_length=40)
    friend3=models.CharField(max_length=40)
    yoursemail=models.EmailField(max_length=50)
    friend1email=models.EmailField(max_length=50)
    friend2email=models.EmailField(max_length=50)
    friend3email=models.EmailField(max_length=50)
class bill(models.Model):
    groupName=models.CharField(max_length=50,primary_key=True)
    totalexpense=models.CharField(max_length=10)
    you=models.CharField(max_length=10)
    friend1=models.CharField(max_length=10)
    friend2=models.CharField(max_length=10)
    friend3=models.CharField(max_length=10)