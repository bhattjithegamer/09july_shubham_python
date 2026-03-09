from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from google.oauth2 import id_token
from google.auth.transport import requests
from .serializers import RegisterSerializer
import uuid
from django.conf import settings
from .models import Product, Order
from django.db import transaction


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['GET'])
@permission_classes([AllowAny])
def get_products(request):
    products = Product.objects.all()
    data = []
    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'category': p.category,
            'stock': p.stock,  # ← આ લાઇન ખાસ ઉમેરો, આના વગર "Out of Stock" જ બતાવશે
            'image': request.build_absolute_uri(p.image.url) if p.image else None
        })
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def google_login(request):
    token = request.data.get('token')
    try:
        CLIENT_ID = settings.GOOGLE_CLIENT_ID
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID, clock_skew_in_seconds=10)
        email = idinfo['email']
        name = idinfo.get('name', '')
        username = email.split('@')[0]
        user, created = User.objects.get_or_create(email=email, defaults={
            'username': username,
            'first_name': name,
        })
        tokens = get_tokens_for_user(user)
        return Response({'tokens': tokens, 'user': {'email': user.email}}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken.'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already registered.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        tokens = get_tokens_for_user(user)
        return Response({'tokens': tokens}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# myapp/views.py માં get_user_profile ફંક્શન સુધારો:

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
        # જો first_name ખાલી હોય તો username મોકલો
        'first_name': user.first_name if user.first_name else user.username,
        'date_joined': user.date_joined.strftime('%d %B %Y'),
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    data = request.data
    user.first_name = data.get('first_name', user.first_name)
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.save()
    return Response({'message': 'Profile updated'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    result = []
    for order in orders:
        result.append({
            'id': order.id,
            'order_id': order.order_id,
            'total_amount': str(order.total_amount),
            'is_paid': order.is_paid,
            'items': order.items,  # product names + qty
            'created_at': order.created_at.strftime('%d %B %Y, %I:%M %p'),
        })
    return Response(result)


# --- CREATE PAYMENT ORDER (Dummy Mode) ---
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment_order(request):
    amount = request.data.get('amount')
    items = request.data.get('items', [])  # [{name, price, quantity}]

    if not amount:
        return Response({'error': 'Amount is required.'}, status=status.HTTP_400_BAD_REQUEST)

    dummy_order_id = f"order_DUMMY_{uuid.uuid4().hex[:14].upper()}"

    Order.objects.create(
        user=request.user,
        total_amount=amount,
        order_id=dummy_order_id,
        items=items,
    )

    return Response({
        'order_id': dummy_order_id,
        'amount': amount,
        'key_id': 'rzp_test_dummy',
    })


# --- PAYMENT SUCCESS ---
# views.py માં handle_payment_success ફંક્શન આ રીતે બદલો:

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def handle_payment_success(request):
    order_id = request.data.get('razorpay_order_id')
    payment_id = request.data.get('razorpay_payment_id')

    if not order_id:
        return Response({'error': 'Missing order ID.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Atomic transaction વાપરવું જેથી જો એક પણ પ્રોડક્ટમાં પ્રોબ્લેમ આવે તો સ્ટોક ના ઘટે
        with transaction.atomic():
            order = Order.objects.select_for_update().get(order_id=order_id)
            
            if order.is_paid:
                return Response({'message': 'Already paid.'})

            # ૧. ઓર્ડરને પેઇડ માર્ક કરો
            order.payment_id = payment_id or f"pay_DUMMY_{uuid.uuid4().hex[:14].upper()}"
            order.is_paid = True
            order.save()

            # ૨. સ્ટોક ઘટાડવાનું લોજિક (Order ના items માંથી)
            for item in order.items:
                p_id = item.get('id')
                qty = int(item.get('quantity', 1))

                if p_id:
                    try:
                        product = Product.objects.select_for_update().get(id=p_id)
                        if product.stock >= qty:
                            product.stock -= qty
                            product.save()
                        else:
                            # જો સ્ટોક ઓછો હોય તો તમે અહીં એરર આપી શકો અથવા લોગ કરી શકો
                            print(f"Low stock for {product.name}")
                    except Product.DoesNotExist:
                        print(f"Product ID {p_id} not found")

            return Response({'message': 'Payment verified and stock updated!'}, status=status.HTTP_200_OK)

    except Order.DoesNotExist:
        return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# --- PAYMENT FAILURE ---
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def handle_payment_failure(request):
    order_id = request.data.get('razorpay_order_id')
    if order_id:
        try:
            order = Order.objects.get(order_id=order_id)
            order.is_paid = False
            order.save()
        except Order.DoesNotExist:
            pass
    return Response({'message': 'Payment failure recorded.'}, status=status.HTTP_200_OK)

# myapp/views.py ના અંતે આ ઉમેરો

@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_details(request, pk):
    """
    Fetch a single product by its ID (pk)
    """
    try:
        product = Product.objects.get(pk=pk)
        return Response({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
            'image': request.build_absolute_uri(product.image.url) if product.image else None
        }, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def custom_login(request):
    from django.contrib.auth import authenticate
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    tokens = get_tokens_for_user(user)
    return Response({
        'access': tokens['access'],
        'refresh': tokens['refresh'],
        'is_admin': user.is_staff or user.is_superuser,
    })




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    user = request.user
    cart_items = request.data.get('items', []) # ફ્રન્ટએન્ડમાંથી આવેલી કાર્ટ આઈટમ્સ
    total_amount = request.data.get('total_amount')

    # Atomic Transaction વાપરવું સારું છે જેથી જો એક પ્રોડક્ટમાં ભૂલ આવે તો આખો ઓર્ડર કેન્સલ થાય
    try:
        with transaction.atomic():
            # ૧. નવો ઓર્ડર બનાવો
            order = Order.objects.create(
                user=user,
                total_amount=total_amount,
                items=cart_items,
                is_paid=True # અથવા પેમેન્ટ વેરિફાઈ થયા પછી
            )

            # ૨. સ્ટોક ઓછો કરવાનું લોજિક
            for item in cart_items:
                product_id = item.get('id')
                quantity_bought = int(item.get('quantity', 1))

                # પ્રોડક્ટ મેળવો
                product = Product.objects.select_for_update().get(id=product_id)

                # સ્ટોક ચેક કરો અને ઓછો કરો
                if product.stock >= quantity_bought:
                    product.stock -= quantity_bought
                    product.save()
                else:
                    # જો સ્ટોક ના હોય તો એરર આપો
                    raise Exception(f"Sorry, {product.name} is out of stock!")

            return Response({"message": "Order placed and stock updated!"}, status=201)

    except Exception as e:
        return Response({"error": str(e)}, status=400)