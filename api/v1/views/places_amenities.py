#!/usr/bin/python3
"""view for the link between Place objects and Amenity objects"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.place import Place
from models.amenity import Amenity


@app_views.route("places/<place_id>/amenities", strict_slashes=False)
def amenities_in_place(place_id):
    """Retrieves the list of all Amenity objects of a Place"""

    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenities = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenities)


@app_views.route("/places/<place_id>/amenities/<amenity_id>", methods=['DELETE'])
def delete_place_amenity(place_id, amenity_id):
    """Deletes a Amenity object to a Place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)

    is_amenity_in_place = False

    for amen in place.amenities:
        if amenity_id == amen.id:
            is_amenity_in_place = True

    if not place or not amenity or not is_amenity_in_place:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route("places/<place_id>/amenities/<amenity_id>", methods=['POST'])
def place_amenity(place_id, amenity_id):
    """Link a Amenity object to a Place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)

    for amen in place.amenities:
        if amenity_id == amen.id:
            return jsonify(amenity.to_dict()), 200

    place.amenities.append(amenity.to_dict())
    storage.save()
    return jsonify(amenity.to_dict()), 201
