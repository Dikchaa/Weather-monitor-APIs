import requests
import json
response=requests.get('https://goweather.herokuapp.com/weather/bangalore')
data=json.loads(response.text)
print(data)
temperature=data.get('temperature')
wind=data.get('wind')
detail=data.get('description')
print(temperature)
print(wind)
print(detail)
