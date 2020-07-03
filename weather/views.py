from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e4ffd5e7ea455ca0b6ad57d3147d3343'

    err_msg = ""
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['city_name']
            existing_city = City.objects.filter(city_name=new_city).count()

            if existing_city == 0:
                response = requests.get(url.format(new_city)).json()

                if response['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist in the world!'

            else:
                err_msg = 'City already exist in the database'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'

    form = CityForm()

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

    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class': message_class
    }

    return render(request, 'weather/home.html', context)


def delete_city(request, cities_name):
    City.objects.get(city_name=cities_name).delete()
    return redirect('index')
