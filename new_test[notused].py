import requests
import json

api_key = "746b57df577be4b85706eebc87f77825"
lat = "48.208176"
lon = "16.373819"
#url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
url = "https://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=746b57df577be4b85706eebc87f77825"

response = requests.get(url)
data = response.json() #json.loads(response.text)
print("data:", data)
print(len(data))
for i in range(0,len(data)+1):
    temperatura = data['list'][i]['main']["temp"]
    humidade    = data['list'][i]['main']["humidity"]
    cidade      = data['list'][i]['name']
    id          = data['list'][i]['id']
    print("\ntemperatura", temperatura)
    print("\nhumidade", humidade)
    print("\ncidade", cidade)
    print("\nid", id)
    


