from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=150, null = False)
    product_price = models.IntegerField(null = False)
    product_image = models.ImageField(upload_to='products', null=False)
    product_category = models.CharField(max_length=150, null = True)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)