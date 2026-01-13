from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

def send_test_email(request):
    if request.method == "POST":
        recipient = request.POST.get("email")
        subject = "Hello from Django & SendGrid"
        message = "This is a test email sent using SendGrid API in a Django Project."
        
        try:
            send_mail(
                subject,
                message,
                None, # Uses DEFAULT_FROM_EMAIL from settings
                [recipient],
                fail_silently=False,
            )
            return render(request, 'email_status.html', {'status': 'Email Sent Successfully!'})
        except Exception as e:
            return render(request, 'email_status.html', {'status': f'Error: {str(e)}'})

    return render(request, 'send_email.html')