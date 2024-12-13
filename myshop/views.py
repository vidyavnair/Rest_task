from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartItem
from myshop.models import Product
from .serializers import CartSerializer,My_serializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    """
    Add a new product to the system.
    """
    if request.method == 'POST':
        serializer = My_serializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({
                "message": "Product added successfully",
                "product": My_serializer(product).data
            }, status=201)
        return Response(serializer.errors, status=400)



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def cart_view(request):
   
    cart, created = Cart.objects.get_or_create(user=request.user)

    if request.method == 'GET':
        
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Add product to cart
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += int(quantity)
        cart_item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update  product in the cart
        cart_item_id = request.data.get('cart_item_id')
        quantity = request.data.get('quantity')

        try:
            cart_item = CartItem.objects.get(id=cart_item_id, cart=cart)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=404)

        cart_item.quantity = int(quantity)
        cart_item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # remove a product from the cart
        cart_item_id = request.data.get('cart_item_id')

        try:
            cart_item = CartItem.objects.get(id=cart_item_id, cart=cart)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=404)

        cart_item.delete()

        serializer = CartSerializer(cart)
        return Response(serializer.data)
