"""

"""
import arrow
from pgeocode import Nominatim
import requests
import os
from dotenv import load_dotenv

# Load API from .env file
load_dotenv()
STORMGLASS_API_KEY = os.getenv("STORMGLASS_API_KEY")
OPEN_WEATHER_API = os.getenv("OPEN_WEATHER_API_KEY")

# This sets the location to US postal codes
nomi = Nominatim('us')


class WeatherData:
    def __init__(self, postal_code):
        # This makes the call to get location data from a postal code
        location_response = nomi.query_postal_code(postal_code)

        # This is all the relevant data from that call
        self.lat = location_response.latitude
        self.lng = location_response.longitude
        self.city_name = location_response.place_name
        self.state_name = location_response.state_name

        # Gets first and last hour of today
        # start = arrow.now().floor('day')
        # end = arrow.now().ceil('day')

        # Now we make a call to the Stormglass API
        # weather_response = getResponse(self.lat, self.lng, start, end)
        weather_response = getOpenWeather(self.lat, self.lng)
        self.json_data = weather_response.json()
        print(self.json_data)


def getResponse(lat, lng, start, end):
    response = requests.get(
        'https://api.stormglass.io/v2/weather/point',
        params={
            'lat': lat,
            'lng': lng,
            'params': ','.join(['airTemperature', 'windSpeed', 'windDirection']),
            'start': start.to('UTC').timestamp(),
            'end': end.to('UTC').timestamp(),
            'source': 'noaa'
        },
        headers={
            'Authorization': STORMGLASS_API_KEY
        }
    )
    return response


def getOpenWeather(lat, lng):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={OPEN_WEATHER_API}&units=imperial'
    )
    return response


if __name__ == "__main__":
    print(WeatherData(32174).json_data)
