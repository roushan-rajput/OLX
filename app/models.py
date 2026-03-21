from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)


class Product(models.Model):
    productname = models.CharField(max_length=100)
    productprice = models.CharField(max_length=100)
    productissue = models.CharField(max_length=200)
    productreason = models.CharField(max_length=200)
    productimg = models.ImageField(upload_to='products/')