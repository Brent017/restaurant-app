import models

from flask import Blueprint, request, jsonify
from flask_login import current_user
from playhouse.shortcuts import model_to_dict

restaurant = Blueprint('restaurant', 'restaurant', url_prefix='/api/v1')

# Index
@restaurant.route('/<id>', methods=["GET"])
def get_all_restaurants(id):
	print("HITTING Index route")
	print(id, "id in index")
	try:
		fav_restaurants = [model_to_dict(restaurant) for restaurant in models.Restaurant.select().where(models.Restaurant.user == id)]
		return jsonify(data=fav_restaurants, status={"code": 200, "message": "Success"})
	except modelsDoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "There was an error gettig the resource"})

# Create
@restaurant.route('/', methods=["POST"])
def create_restaurant():
	print("HITTING CREATE")
	user = current_user.get_id()
	print(user, 'user in create')
	payload = request.get_json()
	print(payload, "payload in create")
	payload['restaurantId'] = payload['id']
	restaurant = models.Restaurant.create(**payload, user=user)

	# print(restaurant.__dict__, 'looking at restaurant model')

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
