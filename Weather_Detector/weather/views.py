from django.shortcuts import render
import json 
import urllib.request
def index(request):
    data = { }
    data2 = { }
    if(request.method == 'POST'):
        city = request.POST['city']
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=ae865bb21af9aaa094561e64952253aa').read()
        json_data = json.loads(res)
        data2 = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
        data["country_code"] = city
        # print(res)

    return(
        render(
            request,
            'index.html',
            {'data': data2}
        )
    )