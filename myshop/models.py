from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):

    Name=models.CharField(max_length=200)
    Description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=3)
    


    def __str__(self) -> str:
        return self.Name
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Reuse the Product table
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.Name}"
