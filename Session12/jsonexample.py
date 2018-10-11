import urllib.request
import json

APIKEY = '8f62260aa7890d58d9a026e2810341ea'
city = 'Wellesley'
country_code = 'us'
url = 'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'.format(
    city=city, country_code=country_code, APIKEY=APIKEY)

#print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text) #loads json in dictionary
#print(response_data)

# How do we get current temperature?


weather = {'coord': {'lon': -71.29, 'lat': 42.3}, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}, {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}, {'id': 741, 'main':
'Fog', 'description': 'fog', 'icon':
'50d'}], 'base': 'stations', 'main':
{'temp': 291, 'pressure': 1005, 'humidity': 90, 'temp_min': 287.05, 'temp_max': 297.05}, 'visibility': 3219, 'wind': {'speed': 3.6, 'deg': 20}, 'rain': {'1h': 2.71}, 'clouds': {'all': 90}, 'dt': 1539286080, 'sys': {'type': 1, 'id': 1273, 'message': 0.013, 'country': 'US', 'sunrise': 1539255256,
'sunset': 1539295701}, 'id': 4954738, 'name': 'Wellesley', 'cod': 200}
#dictionary including temp is a value of main
#main is an element of weather

#print(weather.keys())

print(weather['main'])
print(weather['main']['temp'])