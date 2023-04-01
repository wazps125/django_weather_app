from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')
def results(request):
    city = request.GET['city']
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = '43b152abc82f8cb0e0d517f01cc61826'

    # Set up the parameters for the API call
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    # Make the API call
    response = requests.get(url, params=params)

    # Parse the JSON response into a Python dictionary
    data = response.json()
    return render(request, 'results.html',{'data':data})