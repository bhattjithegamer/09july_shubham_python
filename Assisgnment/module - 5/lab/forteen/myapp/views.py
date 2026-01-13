import requests
from django.shortcuts import render

def get_weather(request):
    weather_data = None
    error_msg = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'your_openweathermap_api_key' 
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                    'humidity': data['main']['humidity'],
                }
            else:
                error_msg = "not_found"
        except Exception as e:
            error_msg = "error"

    return render(request, 'weather.html', {'weather': weather_data, 'error': error_msg})