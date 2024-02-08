from django.db import models
class order_pizza(models.Model):
    product_img=models.ImageField(upload_to='order_pizza/')
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()

class order_burger(models.Model):
    product_img=models.ImageField(upload_to='order_burger/')
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()



# Create your models here.
