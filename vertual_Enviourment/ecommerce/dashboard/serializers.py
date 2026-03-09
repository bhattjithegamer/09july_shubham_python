from rest_framework import serializers
from myapp.models import Product, Order  # અહીં તમારી મેઈન એપનું નામ લખવું (દા.ત. myapp)

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # અથવા જે ફિલ્ડ રાખવા હોય તે

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    # આ લાઈન યુઝરનું સાચું નામ (Username) બતાવશે
    user__username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'