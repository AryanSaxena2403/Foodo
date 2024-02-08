from django.contrib import admin
from django.urls import path,include
from Cart.views import cart_Viewset
from rest_framework import routers
from Cart import views


router=routers.DefaultRouter()
router.register(r'companies',cart_Viewset)

urlpatterns = [
    # path('deals/',views.move_to_cart),
    path('',include(router.urls)),
    path('item/',views.itm,name="itm"),
]