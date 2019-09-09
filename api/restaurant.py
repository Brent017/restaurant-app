import models

from flask import Blueprint, request, jsonify
from flask_login import current_user
from playhouse.shortcuts import model_to_dict

restaurant = Blueprint('restaurant', 'restaurant', url_prefix='/api/v1')

# Index
@restaurant.route('/', methods=["GET"])
def get_all_restaurants():
	try:
		restaurants = [model_to_dict(restaurant) for restaurant in models.Restaurant.select()]
		return jsonify(data=restaurants, status={"code": 200, "message": "Success"})
	except modelsDoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "There was an error gettig the resource"})

# Create
@restaurant.route('/', methods=["POST"])
def create_restaurant():
	payload = request.get_json()
	print(payload, "payload in create")

	restaurant = models.Restaurant.create(**payload)

	print(restaurant.__dict__, 'looking at restaurant model')

	restaurant_dict = model_to_dict(restaurant)

	return jsonify(data=restaurant_dict, status={"code": 201, "message": "Success"})

# Show
@restaurant.route('/<id>', methods=["GET"])
def get_one_restaurant(id):
	restaurant = models.Restaurant.get_by_id(id)

	return jsonify(data=model_to_dict(restaurant), status={"code": 200, "message": "Success"})

# Update route
@restaurant.route('/<id>', methods=["PUT"])
def update_restaurant(id):
	payload = request.get_json()

	query = models.Restaurant.update(**payload).where(models.Restaurant.id == id)
	query.execute()

	updated_restaurant = models.Restaurant.get_by_id(id)

	return jsonify(data=model_to_dict(updated_restaurant), status={"code": 200, "message": "Success"})

# Delete
@restaurant.route('/<id>', methods=["Delete"])
def delete_restaurant(id):
	query = models.Restaurant.delete().where(models.Restaurant.id == id)
	query.execute()

	return jsonify(data='resource successfully deleted', status={"code": 200, "message": "Resource deleted"})
