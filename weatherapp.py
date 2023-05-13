import json
import requests

# Constants
APPID = '*****************************'  #Get your appid from openweathermap.org website
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}'

# Get user input for city name
city = input('Enter city name: ')

# Construct URL for API request
url = BASE_URL.format(city) + '&APPID=' + APPID
print(url)

# Make API request and get response
response = requests.get(url)
response.raise_for_status()

# Load JSON data from response
weather_data = json.loads(response.text)

# Extract relevant data from JSON
location = weather_data['name']
description = weather_data['weather'][0]['description']
temp_kelvin = weather_data['main']['temp']
temp_celsius = round(temp_kelvin - 273.15, 2)
humidity = weather_data['main']['humidity']

# Print weather data to console
print('Weather for {}:'.format(location))
print('Description: {}'.format(description))
print('Temperature: {}°C'.format(temp_celsius))
print('Humidity: {}%'.format(humidity))
