from django.conf import settings
from django.shortcuts import render
from twilio.rest import Client

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

# 1. Send OTP View
def send_otp(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone') # Format: +919876543210
        
        # Twilio creates and sends the code automatically
        verification = client.verify.v2.services(settings.TWILIO_VERIFY_SERVICE_SID) \
            .verifications \
            .create(to=phone_number, channel='sms')
        
        return render(request, 'verify_otp.html', {'phone': phone_number})
    return render(request, 'send_otp.html')

# 2. Check OTP View
def verify_otp(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        otp_code = request.POST.get('otp')
        
        # Twilio checks if the code is correct
        check = client.verify.v2.services(settings.TWILIO_VERIFY_SERVICE_SID) \
            .verification_checks \
            .create(to=phone_number, code=otp_code)
        
        if check.status == 'approved':
            return render(request, 'status.html', {'msg': 'Phone Verified Successfully!'})
        else:
            return render(request, 'status.html', {'msg': 'Invalid OTP. Try again.'})
        
