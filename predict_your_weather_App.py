import requests
from pprint import pprint
#create account on openweather and enter api key
API_Key ='YOUR OWN API KEY'
city= input("Enter a city: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)