import requests
from django.shortcuts import render

def country_info(request):
    country_data = None
    error = None

    if request.method == "POST":
        country_name = request.POST.get("country_name").strip()
        # API Endpoint for searching by name
        url = f"https://restcountries.com/v3.1/name/{country_name}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()[0]  # The API returns a list; take the first match
                
                # Extracting specific data safely
                country_data = {
                    'name': data.get('name', {}).get('common'),
                    'official_name': data.get('name', {}).get('official'),
                    'flag': data.get('flags', {}).get('png'),
                    'capital': data.get('capital', ['N/A'])[0],
                    'region': data.get('region'),
                    'subregion': data.get('subregion'),
                    'population': f"{data.get('population', 0):,}", # Formatting with commas
                    'languages': ", ".join(data.get('languages', {}).values()),
                    'google_maps': data.get('maps', {}).get('googleMaps')
                }
            else:
                error = "Country not found. Please check the spelling."
        except Exception as e:
            error = f"Something went wrong: {str(e)}"

    return render(request, 'country.html', {'country': country_data, 'error': error})