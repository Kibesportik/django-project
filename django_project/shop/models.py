from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    product = models.ForeignKey('shop.Product', related_name='orders', on_delete=models.CASCADE)
    quantity = models.IntegerField()
