from django.shortcuts import render
import requests

def get_joke(request):
    url = "https://official-joke-api.appspot.com/jokes/random"
    joke = {"setup": "No joke found!", "punchline": ""}

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            joke["setup"] = data.get("setup")
            joke["punchline"] = data.get("punchline")
    except requests.exceptions.RequestException:
        joke["setup"] = "Failed to connect to API."

    return render(request, "joke.html", {"joke": joke})