import requests
import math
a = input("enter city name: \n")
apikey = '9cd52d092a8769367d256b35c44d477f'
def getweather(apikey,b):
    url=f'https://api.openweathermap.org/data/2.5/weather?q={b}&appid={apikey}'
    response = requests.get(url).json()
    x=response['main']
    a = x['temp']
    temp = math.floor((a-273))
    statement=response['weather'][1]['main'],response['weather'][1]['description']
    mintemp=x['temp_min']
    maxtemp=x['temp_max']
    pressure =x['pressure']
    humidity = x['humidity']
    visibility=response['visibility']
    wind = response['wind']['speed']
    print(temp,statement,mintemp,maxtemp,pressure,humidity,visibility,wind)
getweather(apikey,a)

