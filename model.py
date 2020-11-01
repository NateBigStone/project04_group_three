from food import get_dish_info
from yelp import api_request
from flickr import get_image


class Foods:
    def __init__(self):
        self.food = ''

    def add_food(self, food):
        self.food = food

    def get_food(self):
        if self.food:
            return self.food

    def get_image(self):
        return get_image(self.food) or None

    def get_recipe(self):
        return get_dish_info(self.food) or None

    def get_yelp(self):
        return api_request(self.food) or None
