from peewee import *
from flask_login import UserMixin
import os
from playhouse.db_url import connect

DATABASE = SqliteDatabase('restaurant.sqlite')

class User(UserMixin, Model):
	username = CharField()
	password = CharField()
	email = CharField()

	class Meta:
		database = DATABASE

class Restaurant(Model):
	restaurantId = IntegerField()
	comments = CharField()
	user = ForeignKeyField(User, backref='restaurant')

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Restaurant] safe=True)
	print("TABLES CREATED")
	DATABASE.close() 