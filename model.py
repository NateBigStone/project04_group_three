from food import get_dish_info
from yelp import api_request


class Foods:
    def __init__(self):
        self.food = ''

    def add_food(self, food):
        self.food = food

    def get_food(self):
        return self.food

    def get_recipe(self):
        return get_dish_info(self.food) or None

    def get_yelp(self):
        return api_request(self.food) or None
