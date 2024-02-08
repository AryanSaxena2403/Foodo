from django.contrib import admin
from order.models import order_pizza,order_burger

class pizza_Admin(admin.ModelAdmin):
    list_display=('product_name','price')
admin.site.register(order_pizza,pizza_Admin)

class burger_Admin(admin.ModelAdmin):
    list_display=('product_name','price')
admin.site.register(order_burger,burger_Admin)

# Register your models here.
