from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Sum
from rest_framework.permissions import AllowAny

# સાચું ઈમ્પોર્ટ: તમારી મેઈન એપ 'myapp' માંથી મોડલ્સ લો
from myapp.models import Product, Order 
from .serializers import ProductSerializer, OrderSerializer

# --- 1. ADMIN DASHBOARD STATS ---
@api_view(['GET'])
@permission_classes([AllowAny])
def admin_statistics(request):
    total_sales = Order.objects.filter(is_paid=True).aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    
    recent_orders = Order.objects.order_by('-created_at')[:5]
    serializer = OrderSerializer(recent_orders, many=True)
    
    return Response({
        'sales': total_sales,
        'orders': total_orders,
        'products': total_products,
        'recent_orders': serializer.data
    })

# --- 2. PRODUCT LIST ---
@api_view(['GET'])
@permission_classes([AllowAny])
def admin_list_products(request):
    products = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# --- 3. ADD PRODUCT ---
@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def admin_add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- 4. EDIT PRODUCT ---
@api_view(['PATCH', 'PUT'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def admin_edit_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- 5. DELETE PRODUCT ---
@api_view(['DELETE'])
@permission_classes([AllowAny])
def admin_delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

# --- 6. ALL ORDERS LIST ---
@api_view(['GET'])
@permission_classes([AllowAny])
def admin_list_orders(request):
    orders = Order.objects.order_by('-created_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

# --- 7. UPDATE ORDER STATUS ---
# views.py માં ફેરફાર
# views.py માં આ મુજબ ફેરફાર કરો
@api_view(['PATCH', 'PUT'])
@permission_classes([AllowAny])
def admin_update_order(request, pk):
    try:
        # ઓર્ડર શોધો
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    # request.data માંથી ડેટા લાવો
    is_paid = request.data.get('is_paid')
    status_val = request.data.get('status')

    # જો ડેટા મોકલ્યો હોય તો જ અપડેટ કરો
    if is_paid is not None:
        order.is_paid = is_paid
        
    if status_val is not None:
        order.status = status_val

    try:
        order.save()
        return Response({
            'id': order.id, 
            'is_paid': order.is_paid, 
            'status': order.status
        }, status=status.HTTP_200_OK)
    except Exception as e:
        # જો કોઈ બીજી એરર આવે તો તે પ્રિન્ટ થશે
        print(f"Error saving order: {e}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)