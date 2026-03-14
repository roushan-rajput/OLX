from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    contact=models.IntegerField()
    city=models.CharField(max_length=50)
    password=models.CharField(max_length=6)
    cpassword=models.CharField(max_length=6)