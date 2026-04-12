from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='buyer')

    
class Product(models.Model):
    productname = models.CharField(max_length=100)
    productprice = models.CharField(max_length=100)
    productissue = models.CharField(max_length=200)
    productreason = models.CharField(max_length=200)
    productimg = models.ImageField(upload_to='products/')
    seller_email = models.CharField(max_length=100, null=True, blank=True)


class Message(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    message = models.TextField()
    product_id = models.IntegerField()   # 🔥 ADD THIS
    timestamp = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.sender + " -> " + self.receiver
    
class Order(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    amount = models.IntegerField()
    razorpay_order_id = models.CharField(max_length=200)
    razorpay_payment_id = models.CharField(max_length=200, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=300, blank=True, null=True)

    paid = models.BooleanField(default=False)