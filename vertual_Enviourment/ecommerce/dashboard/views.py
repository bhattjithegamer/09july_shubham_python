from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from myapp.models import Product, Order


# --- 1. ADMIN DASHBOARD STATS ---
@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_statistics(request):
    total_sales = Order.objects.filter(is_paid=True).aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    recent_orders = Order.objects.order_by('-created_at')[:5].values(
        'id', 'user__username', 'total_amount', 'is_paid', 'created_at'
    )
    return Response({
        'sales': total_sales,
        'orders': total_orders,
        'products': total_products,
        'recent_orders': list(recent_orders)
    })


# --- 2. PRODUCT LIST ---
@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_list_products(request):
    products = Product.objects.all().values('id', 'name', 'price', 'description')
    return Response(list(products))


# --- 3. ADD PRODUCT ---
@api_view(['POST'])
@permission_classes([IsAdminUser])
def admin_add_product(request):
    name = request.data.get('name')
    price = request.data.get('price')
    description = request.data.get('description', '')

    if not name or not price:
        return Response({'error': 'Name and price are required.'}, status=status.HTTP_400_BAD_REQUEST)

    product = Product.objects.create(name=name, price=price, description=description)
    return Response({'id': product.id, 'name': product.name, 'price': str(product.price)}, status=status.HTTP_201_CREATED)


# --- 4. EDIT PRODUCT ---
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def admin_edit_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    product.name = request.data.get('name', product.name)
    product.price = request.data.get('price', product.price)
    product.description = request.data.get('description', product.description)
    product.save()
    return Response({'id': product.id, 'name': product.name, 'price': str(product.price)})


# --- 5. DELETE PRODUCT ---
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def admin_delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({'msg': 'Product removed.'}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({'error': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


# --- 6. ALL ORDERS LIST ---
@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_list_orders(request):
    orders = Order.objects.order_by('-created_at').values(
        'id', 'order_id', 'user__username', 'total_amount', 'is_paid', 'payment_id', 'created_at'
    )
    return Response(list(orders))


# --- 7. UPDATE ORDER STATUS ---
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def admin_update_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

    order.is_paid = request.data.get('is_paid', order.is_paid)
    order.save()
    return Response({'id': order.id, 'is_paid': order.is_paid})

