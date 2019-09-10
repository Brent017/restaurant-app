import models

import os
import sys
import secrets

from flask import Blueprint, request, jsonify, url_for, send_file
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user', url_prefix='/user')

# Register
@user.route('/register', methods=["POST"])
def register():
	payload = request.form.to_dict()
	payload['email'].lower()
	try:
		models.User.get(models.User.username == payload['username'])
		return jsonify(data={}, status={"code": 401, "message": "A user with that username already exists"})
	except models.DoesNotExist:
		payload['password'] = generate_password_hash(payload['password'])
		user = models.User.create(**payload)

		login_user(user)
		user_dict = model_to_dict(user)
		print(user_dict)
		print(type(user_dict))
		del user_dict['password']
		return jsonify(data=user_dict, status={"code": 201, "message": "Success"})

# Login
@user.route('/login', methods=["POST"])
def login():
	payload = request.get_json()
	print(payload, '<--payload in login')
	try: 
		user = models.User.get(models.User.username == payload['username'])
		user_dict = model_to_dict(user)
		if(check_password_hash(user_dict['password'], payload['password'])):
			del user_dict['password']
			login_user(user)
			print(user, 'this is user in login')
			return jsonify(data=user_dict, status={"code": 200, "message": "Success"})
		else:
			return jsonify(data={}, status={"code": 401, "message": "Username or password is incorrect"})
	except models.DoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "Username or password is incorrect"})

# Get user favorites
@user.route('<id>/restaurants', methods=["GET"])
def get_user_restaurants(id):
	user = models.User.get_by_id(id)
	print(user.restaurants, 'users restaurants')

	restaurants = [model_to_dict(restaurants) for restaurant in restaurant.user]

	def delete_key(item, key):
		restaurants_without_user = [delete_key(restaurants, 'user') for restaurants in restaurants]

		return jsonify(data=restaurants, status={"code": 201, "message": "Success"})

# Logout
@user.route('/logout')
def logout():
	logout_user()
	return redirect('/login')




