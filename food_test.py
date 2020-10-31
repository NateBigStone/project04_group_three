import unittest
import food
from unittest import TestCase
from unittest.mock import patch

class TestFoodApi(TestCase):

    #User input validation based on return value using ".isalpha".
    def test_user_input_is_alpha(self):
        self.assertTrue(food.get_dish().isalpha)

    #Mocks response and checks that the name and ingredients are properly grabbed from the json data.
    @patch('requests.get')
    def test_response(self, mock_requests_get):
        example_api_response = {"q":"chicken","from":0,"to":10,"more":True,"count":120230,"hits":[{"recipe":{"uri":"http://www.edamam.com/ontologies/edamam.owl#recipe_b79327d05b8e5b838ad6cfd9576b30b6","label":"Chicken Vesuvio","image":"https://www.edamam.com/web-img/e42/e42f9119813e890af34c259785ae1cfb.jpg","source":"Serious Eats","url":"http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html","shareAs":"http://www.edamam.com/recipe/chicken-vesuvio-b79327d05b8e5b838ad6cfd9576b30b6/chicken","yield":4.0,"dietLabels":["Low-Carb"],"healthLabels":["Peanut-Free","Tree-Nut-Free"],"cautions":["Sulfites"],"ingredientLines":["1/2 cup olive oil","5 cloves garlic, peeled","2 large russet potatoes, peeled and cut into chunks","1 3-4 pound chicken, cut into 8 pieces (or 3 pound chicken legs)","3/4 cup white wine","3/4 cup chicken stock","3 tablespoons chopped parsley","1 tablespoon dried oregano","Salt and pepper","1 cup frozen peas, thawed"]}}]}

        mock_requests_get().json.return_value = example_api_response
        converted = food.convert_response(example_api_response)
        expected_dish = next(iter(converted))

        self.assertEqual(expected_dish,"Chicken Vesuvio")

    #Mocks response with 0 hits, checks for empty dict.
    @patch('requests.get')
    def test_response_no_hits(self, mock_requests_get):
        example_api_response = {'q': 'notrealdish', 'from': 0, 'to': 10, 'more': False, 'count': 0, 'hits': []}
        mock_requests_get().json.return_value = example_api_response
        converted = food.convert_response(example_api_response)

        self.assertEqual(converted,{})
        
    #Uses example input that realistically nobody is ever going to type in, if not found in cache "None" is returned.    
    def test_not_in_cache(self):
        self.example_input = "ThisIsNotGoingToBeFoundInCache"
        test_not_found = food.check_cache(self.example_input)
        if test_not_found == None:
            print("Not found in cache")

        self.assertEqual(test_not_found, None)

    #Mocks response.status_code, if not equal to 200 then "error" is returned.
    @patch('requests.get')
    def test_request_response_status_code(self, mock_requests_get):
        mock_requests_get.return_value.status_code = 404 # Mock status code of response.
        response = food.request_dishes("Example")

        self.assertEqual(response, "error")
