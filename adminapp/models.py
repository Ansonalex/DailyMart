from django.db import models
class PRODUCTS(models.Model):
    productname=models.CharField(max_length=10)
    productimage=models.ImageField(upload_to="productimage")
    productprice=models.IntegerField()
    category=models.CharField(max_length=10,)
class CATEGORIES(models.Model):
    category=models.CharField(max_length=10)
    categoryimage=models.ImageField(upload_to="categoryimage")
    categorydiscription=models.CharField(max_length=10)

# Create your models here.
