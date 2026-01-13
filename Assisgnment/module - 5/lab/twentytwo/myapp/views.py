import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

def checkout_page(request):
    return render(request, 'checkout.html', {
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY
    })

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        domain_url = "http://localhost:8000/" # Change to your live domain in production
        try:
            # Create a Stripe Checkout Session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': 2000, # Amount in cents ($20.00)
                            'product_data': {
                                'name': 'Consultation Fee',
                                'description': 'Medical consultation with Dr. Smith',
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=domain_url + 'payment/success/',
                cancel_url=domain_url + 'payment/cancelled/',
            )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)})

def payment_success(request):
    return render(request, 'success.html')

def payment_cancelled(request):
    return render(request, 'cancelled.html')