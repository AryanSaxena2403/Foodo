from django.db import models

# Create your models here.
class product_cart(models.Model):
    product_img=models.ImageField(upload_to='cart/')
    product_name=models.CharField(max_length=50)
    qty=models.IntegerField()
    price=models.IntegerField()
