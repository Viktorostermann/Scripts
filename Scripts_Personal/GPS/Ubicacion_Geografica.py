import pywhatkit.core
import sqlite3
from geolite import GeoLite2

def get_location():
    location = GeoLite2.get_instance()
    location.setCoordinates(37.7749, -122.4194)  # Example: San Francisco
    while True:
        latitude = location.latitude
        longitude = location.longitude
        print(f"Ubicación:", f"{latitude}, {longitude}")

get_location()