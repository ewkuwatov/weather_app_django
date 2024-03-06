from django.shortcuts import render
import requests


def get_weather(city):
    api_key = '65ba6faa407e4dfb9664b0f3b1ef1235'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather(city)

        url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
        response = requests.get(url)
        data = response.json()

        # Обработка данных и выбор нужных вам валют
        currencies = {
            "US Dollar": data[0]["Rate"],
            "Euro": data[1]["Rate"],
            "Ruble": data[2]["Rate"],
            "Pound Sterling": data[3]["Rate"],
            "Japan Yen": data[4]["Rate"],
            "Argentine Peso": data[5]["Rate"],
        }
        return render(request, 'app/index.html', {'weather_data': weather_data,
                                                                     'currencies': currencies})
    else:
        return render(request, 'app/index.html')


