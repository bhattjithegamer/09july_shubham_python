from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # આપણે નક્કી કરેલી કેટેગરીઝ
    CATEGORY_CHOICES = [
        ('Elite Laptops', 'Elite Laptops'),
        ('Mechanical Keyboards', 'Mechanical Keyboards'),
        ('Pro Peripherals', 'Pro Peripherals'),
        ('Workstation Setup', 'Workstation Setup'),
    ]

    name = models.CharField(max_length=200)
    stock = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Elite Laptops') # આ નવું ઉમેરો
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Razorpay Payment Details
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    order_id = models.CharField(max_length=100, null=True, blank=True)

    # Products purchased — stored as JSON list of {name, price, quantity}
    items = models.JSONField(default=list, blank=True)

    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
# myapp/models.py

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    order_id = models.CharField(max_length=100, null=True, blank=True)
    items = models.JSONField(default=list, blank=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ✅ આ લાઇન નવી ઉમેરો
    status = models.CharField(
        max_length=20, 
        default='Pending',
        choices=[
            ('Pending', 'Pending'),
            ('Processing', 'Processing'),
            ('Shipped', 'Shipped'),
            ('Delivered', 'Delivered'),
            ('Cancelled', 'Cancelled'),
        ]
    )

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"