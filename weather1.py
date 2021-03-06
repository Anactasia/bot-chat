import os
import requests
import json
import pprint

API_KEY = '698b85e113937b14297f5582f941d0a7'


def get_weather(query):
    if not query:
        query = 'fetch:ip'
    response = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': query, 'type': 'like', 'units': 'metric', 'APPID': API_KEY})
    if response.status_code == 200:
        data = response.json()

        return [data['list'][0]['weather'][0]['description'],
                data['list'][0]['main']['temp'], data['list'][0]['weather'][0]['icon']]

