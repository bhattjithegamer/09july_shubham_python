from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Sum
from myapp.models import Product, Order 
from .serializers import ProductSerializer, OrderSerializer
from myapp.views import get_tokens_for_user


# --- 1. ADMIN DASHBOARD STATS ---
@api_view(['GET'])
@permission_classes([AllowAny])
def admin_statistics(request):
    total_sales = Order.objects.filter(is_paid=True).aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    
    recent_orders = Order.objects.order_by('-created_at')[:5]
    serializer = OrderSerializer(recent_orders, many=True)

    top_products_raw = {}
    for order in Order.objects.filter(is_paid=True):
        for item in (order.items or []):
            name = item.get('name', 'Unknown')
            qty  = int(item.get('quantity', 1))
            top_products_raw[name] = top_products_raw.get(name, 0) + qty

    top_products = sorted(
        [{"name": k, "sold": v} for k, v in top_products_raw.items()],
        key=lambda x: x["sold"],
        reverse=True
    )[:10]

    return Response({
        'sales': total_sales,
        'orders': total_orders,
        'products': total_products,
        'recent_orders': serializer.data,
        'top_products': top_products,
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
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

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
@api_view(['PATCH', 'PUT'])
@permission_classes([AllowAny])
def admin_update_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    is_paid = request.data.get('is_paid')
    status_val = request.data.get('status')

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
        print(f"Error saving order: {e}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# --- 8. ADMIN LOGIN ---
@api_view(['POST'])
@permission_classes([AllowAny])
def admin_login(request):
    from django.contrib.auth import authenticate
    from django.contrib.auth.models import User

    username = request.data.get('username', '').strip()
    password = request.data.get('password', '').strip()

    if username != 'shubham':
        return Response(
            {'error': 'Invalid credentials.'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    user, created = User.objects.get_or_create(username='shubham')
    if created:
        user.set_password('bhatt')
        user.save()

    if not user.check_password(password):
        return Response(
            {'error': 'Invalid credentials.'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    tokens = get_tokens_for_user(user)
    return Response({
        'access':   tokens['access'],
        'refresh':  tokens['refresh'],
        'is_admin': True,
    }, status=status.HTTP_200_OK)


# --- 9. ADMIN CHANGE PASSWORD ---
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def admin_change_password(request):
    current_password = request.data.get('current_password', '').strip()
    new_password     = request.data.get('new_password', '').strip()

    if not current_password or not new_password:
        return Response({'error': 'Both fields required.'}, status=status.HTTP_400_BAD_REQUEST)

    if not request.user.check_password(current_password):
        return Response({'error': 'Current password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

    if len(new_password) < 4:
        return Response({'error': 'Password must be at least 4 characters.'}, status=status.HTTP_400_BAD_REQUEST)

    request.user.set_password(new_password)
    request.user.save()

    return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)