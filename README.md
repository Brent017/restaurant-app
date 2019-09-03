# restaurant-app
Finds restaurant menus near user

## User Story-
### MVP:
  * User will be able to login using unique username and hashed password.
  * User will be able to search for restaurants nearby.
  * User will be able to add (create) a favorite restaurant with info on what they like.
  * User will be able to read their list of favorites.
  * User will be able to edit their list of favorites.
  * User will be able to delete a restaurant from their list.

### Stretch:
  * User can upload photos of food.
  * User reviews of restaurants with full CRUD functionality.
  * User can view other users reviews of restaurants.
  * App will be nicely styled.
  * Integrate API to return menu from selected restaurant.
  * Integrate text reader to verbalize menu for visually impaired users

|URL        | HTTP Verb | Action | Description       |
|-----------|:---------:|:------:|:------------------|
|/favorites/    | GET       | index  | Show all favorites    |
|/favorites/new | GET       | new    | Show new form     |
|/favorites     | POST      | create | Create a favorite    |
|/favorites/:id | GET       | show   | Show favorite with :id|
|/favorites/:id/edit| GET   | edit   | Show edit form for favorite with :id|
|/favorites/:id | PUT     | update | Update favorite with :id |
|/favorites/:id | DELETE    | destroy| Delete favorite with :id|
