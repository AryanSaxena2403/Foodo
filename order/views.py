from django.shortcuts import render
from order.models import order_burger,order_pizza

def order(request):
    orderp=order_pizza.objects.all()
    orderb=order_burger.objects.all()
    data={
        'orderp':orderp,
        'orderb':orderb
    }
    return render(request,"menu.html",data)

# Create your views here.
