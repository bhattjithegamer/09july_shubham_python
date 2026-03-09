from rest_framework import serializers
from myapp.models import Product, Order  

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    user__username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'