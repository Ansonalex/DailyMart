from django.db import models
from adminapp.models import*
class REG(models.Model):
    Username=models.CharField(max_length=10)
    EmailAddress=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    ConfirmPassword=models.CharField(max_length=10)
class CONTACTS(models.Model):
    Name=models.CharField(max_length=10)
    EmailAddress=models.CharField(max_length=10)
    Phonenumber=models.IntegerField()
    Address=models.CharField(max_length=10)
class CART(models.Model):
    userid=models.ForeignKey(REG,on_delete=models.CASCADE)
    productid=models.ForeignKey(PRODUCTS,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0)
class CHECKOUT(models.Model):
    userid=models.ForeignKey(REG,on_delete=models.CASCADE)
    cartid=models.ForeignKey(CART,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=10)
    city=models.CharField(max_length=15)
    state=models.CharField(max_length=10,default="")
    country=models.CharField(max_length=10)
    postalzip=models.CharField(max_length=10)
    

# Create your models here.
