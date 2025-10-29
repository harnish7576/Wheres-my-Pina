from flask import Blueprint, request, jsonify
from app.services.places_service import get_nearby_pina_places

main = Blueprint('main', __name__)

@main.route('/api/nearby', methods=['POST'])
def nearby_places():
    data = request.get_json()
    lat = data.get('lat')
    lng = data.get('lng')
    location = data.get('location')

    try:
        results = get_nearby_pina_places(lat=lat, lng=lng, location=location)
        return jsonify({"places": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
