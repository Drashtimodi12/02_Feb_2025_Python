from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    """
    Model representing a product category.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category_image = models.ImageField(upload_to='categories/', blank=True, null=True)

    

class Product(models.Model):
    """
    Model representing a product.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    
    

class Cart(models.Model):
    """
    Model representing a user's shopping cart.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price*self.quantity

   
    
class Order(models.Model):
    """
    Model representing an order placed by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

   
    
class OrderItem(models.Model):
    """
    Model representing an item in an order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

   
    
    def total_price(self):
        return self.product.price*self.quantity

