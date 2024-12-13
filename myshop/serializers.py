from rest_framework import serializers
from .models import Cart, CartItem
from. models import Product

class My_serializer(serializers.ModelSerializer):

    class Meta:
            model=Product
            fields='__all__'
class CartItemSerializer(serializers.ModelSerializer):
    product = My_serializer()  # Product details in the cart item

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at']