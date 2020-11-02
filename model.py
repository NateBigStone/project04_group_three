from food import get_dish_info
from yelp import api_request
from flickr import get_image
from database import add_data, return_all, delete_record
import json
import ast


class Foods:
    def __init__(self):
        self.food = ''
        self.image = None
        self.recipe = None
        self.restaurant = None

    def add_food(self, food):
        self.food = food

    def get_food(self):
        if self.food:
            return self.food

    def get_image(self):
        self.image = get_image(self.food) or None
        return self.image

    def get_recipe(self):
        self.recipe = get_dish_info(self.food) or None
        if self.recipe:
            # converts recipe from dictionary to string
            recipe_string = json.dumps(self.recipe)
        else:
            recipe_string = None
        self.recipe = recipe_string
        return self.recipe

    def get_yelp(self):
        self.restaurant = api_request(self.food) or None
        return self.restaurant

    def save_bookmark(self):
        add_data(self.restaurant, self.recipe, self.image)

    def get_all_food(self):
        # returns a list of "Foods" objects. For each entry, [0] = restaurant, [1] = recipe, [2] = flickr url
        results = return_all()
        return results

    def delete_food(self, restaurant, recipe, image):
        # removes the selected Food object from the database
        delete_record(restaurant, recipe, image)
