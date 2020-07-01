from django.shortcuts import render, get_object_or_404
import requests
from .models import City

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e4ffd5e7ea455ca0b6ad57d3147d3343'
    city = 'Abuja'



    cities = City.objects.all()
    weather_data = []

    for city in cities:
        response = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.city_name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon']
        }

    weather_data.append(city_weather)

    return render(request, 'weather/home.html', {'weather_data': weather_data})

