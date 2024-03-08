from django.shortcuts import render
import requests

def get_weather(city):
    api_key = '65ba6faa407e4dfb9664b0f3b1ef1235'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def get_currency_rates():
    url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'
    response = requests.get(url)
    data = response.json()
    # Extracting the first 6 currency rates
    currency_data = data[:6]
    return currency_data

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather(city)
        currency_data = get_currency_rates()

        return render(request, 'app/index.html', {'weather_data': weather_data, 'currency_data': currency_data})
    else:
        return render(request, 'app/index.html')
