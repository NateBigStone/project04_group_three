import unittest
import food
from unittest import TestCase
from unittest.mock import patch

class TestFoodApi(TestCase):

    def test_user_input(self):
        self.assertTrue(food.get_dish().isalnum)

    @patch('requests.get')
    def test_response(self, mock_requests_get):
        example_api_response = {"q":"chicken","from":0,"to":10,"more":True,"count":120230,"hits":[{"recipe":{"uri":"http://www.edamam.com/ontologies/edamam.owl#recipe_b79327d05b8e5b838ad6cfd9576b30b6","label":"Chicken Vesuvio","image":"https://www.edamam.com/web-img/e42/e42f9119813e890af34c259785ae1cfb.jpg","source":"Serious Eats","url":"http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html","shareAs":"http://www.edamam.com/recipe/chicken-vesuvio-b79327d05b8e5b838ad6cfd9576b30b6/chicken","yield":4.0,"dietLabels":["Low-Carb"],"healthLabels":["Peanut-Free","Tree-Nut-Free"],"cautions":["Sulfites"],"ingredientLines":["1/2 cup olive oil","5 cloves garlic, peeled","2 large russet potatoes, peeled and cut into chunks","1 3-4 pound chicken, cut into 8 pieces (or 3 pound chicken legs)","3/4 cup white wine","3/4 cup chicken stock","3 tablespoons chopped parsley","1 tablespoon dried oregano","Salt and pepper","1 cup frozen peas, thawed"]}}]}

        mock_requests_get().json.return_value = example_api_response
        converted = food.convert_response(example_api_response)
        expected_dish = next(iter(converted))

        self.assertEqual(expected_dish,"Chicken Vesuvio")

    @patch('requests.get')
    def test_response_no_hits(self, mock_requests_get):
        example_api_response = {'q': 'notrealdish', 'from': 0, 'to': 10, 'more': False, 'count': 0, 'hits': []}
        mock_requests_get().json.return_value = example_api_response
        converted = food.convert_response(example_api_response)

        self.assertEqual(converted,{})
        