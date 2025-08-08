# a python program that is the inverse of zip.py
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

geolocator = Nominatim(user_agent="m0ss")

try:
    location = geolocator.geocode("Brown Ave, Prospect Park, New Jersey", addressdetails=True, timeout=10)
    if location and "postcode" in location.raw['address']:
        print("Postal Code: ", location.raw['address']['postcode'])
    else:
        print("Postal code not found")

except (GeocoderTimedOut, GeocoderUnavailable) as e:
    print(f"Postal code not found: {e}")

