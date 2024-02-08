from django.shortcuts import render,redirect
from Cart.models import product_cart
from rest_framework import viewsets
from Cart.serializers import cart_Api
# Create your views here.
# def move_to_cart(request):
#     if request.method=='POST':
#         product_img=request.POST.get('name')
#         product_name=request.POST.get('order')
#         qty=request.POST.get('qty')
#         price=request.POST.get('price')
#         en=product_cart(product_img=product_img,product_name=product_name,qty=qty,price=price)
#         en.save()

#         return redirect("index.html")
class cart_Viewset(viewsets.ModelViewSet):
    queryset=product_cart.objects.all()
    serializer_class=cart_Api



def itm(request):
    return render(request,"cart.html")

