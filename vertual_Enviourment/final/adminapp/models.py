from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Gaming Laptop', 'Gaming Laptop'),
    ('Ultrabook', 'Ultrabook'),
    ('MacBook', 'MacBook'),
    ('Business Laptop', 'Business Laptop'),
    ('Student Laptop', 'Student Laptop'),
    ('Workstation Laptop', 'Workstation Laptop'),
    ('2-in-1 Laptop', '2-in-1 Laptop'),
    ('Convertible Laptop', 'Convertible Laptop'),
    ('Budget Laptop', 'Budget Laptop'),
    ('Premium Laptop', 'Premium Laptop'),
    ('Chromebook', 'Chromebook'),
    ('Creator Laptop', 'Creator Laptop'),
    ('AI Laptop', 'AI Laptop'),
    ('Touchscreen Laptop', 'Touchscreen Laptop'),
    ('Thin & Light Laptop', 'Thin & Light Laptop'),
    ('Rugged Laptop', 'Rugged Laptop'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    processor = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    graphics = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
