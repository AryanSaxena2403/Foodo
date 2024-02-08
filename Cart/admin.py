from django.contrib import admin
from Cart.models import product_cart

class Cart_Admin(admin.ModelAdmin):
    list_display=('product_name','qty','price')

admin.site.register(product_cart,Cart_Admin)

# Register your models here.
