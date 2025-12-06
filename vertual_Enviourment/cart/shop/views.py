# store/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Home Page View
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# Add to Cart View
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    # Jo product already hoy to quantity vadharo, nahitar navi add karo
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    
    request.session['cart'] = cart
    return redirect('cart_detail')

# Cart Page View
def cart_detail(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    
    cart_items = []
    total_price = 0

    for product in products:
        quantity = cart[str(product.id)]
        total = product.price * quantity
        total_price += total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total
        })

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})