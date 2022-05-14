"""

"""
import arrow
from pgeocode import Nominatim
import requests
import os
from dotenv import load_dotenv

#
load_dotenv()
STORMGLASS_API_KEY = os.getenv("STORMGLASS_API_KEY")

#
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
        start = arrow.now().floor('day')
        end = arrow.now().ceil('day')

        # Now we make a call to the Stormglass API
        weather_response = getResponse(self.lat, self.lng, start, end)
        self.json_data = weather_response.json()


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


if __name__ == "__main__":
    print(WeatherData(32174).json_data)
