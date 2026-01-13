import googlemaps
from django.conf import settings
from django.shortcuts import render

def map_view(request):
    context = {
        'api_key': settings.GOOGLE_MAPS_API_KEY,
        'distance': None,
        'duration': None,
    }

    if request.method == "POST":
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')

        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

        try:
            # 1. Use Distance Matrix API
            result = gmaps.distance_matrix(origin, destination, mode='driving')

            if result['rows'][0]['elements'][0]['status'] == 'OK':
                element = result['rows'][0]['elements'][0]
                context['distance'] = element['distance']['text']
                context['duration'] = element['duration']['text']
                context['origin_addr'] = result['origin_addresses'][0]
                context['dest_addr'] = result['destination_addresses'][0]
            else:
                context['error'] = "Locations not found or route unavailable."
        except Exception as e:
            context['error'] = f"API Error: {str(e)}"

    return render(request, 'maps.html', context)