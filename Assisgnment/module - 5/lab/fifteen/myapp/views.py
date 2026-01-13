import requests
from django.shortcuts import render

def get_location(request):
    result = None
    error_msg = None

    if request.method == 'POST':
        address = request.POST.get('address')
        
        url = f'https://nominatim.openstreetmap.org/search?q={address}&format=json&limit=1'
        headers = {'User-Agent': 'DjangoGeocodingApp/1.0'}

        try:
            response = requests.get(url, headers=headers)
            data = response.json()

            if data:
                result = {
                    'address': address,
                    'lat': data[0]['lat'],
                    'lon': data[0]['lon'],
                    'display_name': data[0]['display_name']
                }
            else:
                error_msg = "Address not found. Please try a different location."
        except Exception as e:
            error_msg = "Error connecting to the geocoding service."

    return render(request, 'location.html', {'result': result, 'error': error_msg})