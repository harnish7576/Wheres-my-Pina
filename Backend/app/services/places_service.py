import requests
import os


YELP_API_KEY = os.getenv("YELP_API_KEY")
YELP_SEARCH_URL = "https://api.yelp.com/v3/businesses/search"

def get_nearby_pina_places(lat=None, lng=None, location=None):
    
    if location and (not lat or not lng):
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="pina_app")
        loc = geolocator.geocode(location)
        if loc:
            lat, lng = loc.latitude, loc.longitude
        else:
            raise ValueError("Invalid location provided")

    headers = {
        "Authorization": f"Bearer {YELP_API_KEY}"
    }

    params = {
        "term": "pina colada",
        "latitude": lat,
        "longitude": lng,
        "radius": 10000,
        "limit": 5
    }

    response = requests.get(YELP_SEARCH_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    for business in data.get("businesses", []):
        results.append({
            "id": business.get("id"),
            "name": business.get("name"),
            "address": ", ".join(business.get("location", {}).get("display_address", [])),
            "distance_meters": business.get("distance"),
            "rating": business.get("rating"),
            "thumbnail_url": business.get("image_url"),
            "featured": False
        })

    return results