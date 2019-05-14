# Note on Google Geocoding
import requests

MAPS_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?key=API_KEY"

params = {'address': 'Bengaluru'}

req = requests.get(MAPS_API_URL, params=params).json()

coordinates = req['results'][0]['geometry']['location']

latitude = coordinates['lat']
longitude = coordinates['lng']

print(latitude, longitude)
