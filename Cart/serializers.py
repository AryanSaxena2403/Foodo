from Cart.models import product_cart
from rest_framework import serializers

class cart_Api(serializers.HyperlinkedModelSerializer):
    product_img=serializers.ImageField(required=False, use_url=True)
    class Meta:
        model=product_cart
        fields=("id","product_img","product_name","qty","price")