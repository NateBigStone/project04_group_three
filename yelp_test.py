import unittest
from unittest import TestCase
from unittest.mock import patch, call
import yelp

class TestYelp(TestCase):

    # Testing API response for restaurant name to match 
    @patch('requests.get')
    def test_restaurant_name(self, mock_requests_get):
        mock_name = 'Revival'
        example_api_response = {'businesses': [{'id': '5K82sS0qi4hCnNXzc0mM3A', 'alias': 'revival-minneapolis', 'name': 'Revival', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/JkWblFghKi0DgZNUbvevcQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/revival-minneapolis?adjust_creative=xU677u-VOS4Ysa92q5sRwg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=xU677u-VOS4Ysa92q5sRwg', 'review_count': 1020, 'categories': [{'alias': 'southern', 'title': 'Southern'}, {'alias': 'sandwiches', 'title': 'Sandwiches'}, {'alias': 'bars', 'title': 'Bars'}], 'rating': 4.0, 'coordinates': {'latitude': 44.925208, 'longitude': -93.27771}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '4257 Nicollet Ave', 'address2': '', 'address3': '', 'city': 'Minneapolis', 'zip_code': '55409', 'country': 'US', 'state': 'MN', 'display_address': ['4257 Nicollet Ave', 'Minneapolis, MN 55409']}, 'phone': '+16123454516', 'display_phone': '(612) 345-4516', 'distance': 4599.481096631084}], 'total': 4200, 'region': {'center': {'longitude': -93.2904052734375, 'latitude': 44.96558443188442}}}
        mock_requests_get().json.return_value = example_api_response
        name = example_api_response['businesses'][0]['name']
        self.assertEqual(mock_name, name)

    # Testing API response for restaurant name to not match
    @patch('requests.get')
    def test_restaurant_name_false(self, mock_requests_get):
        mock_name = 'Chuck E. Cheese'
        example_api_response = {'businesses': [{'id': '5K82sS0qi4hCnNXzc0mM3A', 'alias': 'revival-minneapolis', 'name': 'Revival', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/JkWblFghKi0DgZNUbvevcQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/revival-minneapolis?adjust_creative=xU677u-VOS4Ysa92q5sRwg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=xU677u-VOS4Ysa92q5sRwg', 'review_count': 1020, 'categories': [{'alias': 'southern', 'title': 'Southern'}, {'alias': 'sandwiches', 'title': 'Sandwiches'}, {'alias': 'bars', 'title': 'Bars'}], 'rating': 4.0, 'coordinates': {'latitude': 44.925208, 'longitude': -93.27771}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '4257 Nicollet Ave', 'address2': '', 'address3': '', 'city': 'Minneapolis', 'zip_code': '55409', 'country': 'US', 'state': 'MN', 'display_address': ['4257 Nicollet Ave', 'Minneapolis, MN 55409']}, 'phone': '+16123454516', 'display_phone': '(612) 345-4516', 'distance': 4599.481096631084}], 'total': 4200, 'region': {'center': {'longitude': -93.2904052734375, 'latitude': 44.96558443188442}}}
        mock_requests_get().json.return_value = example_api_response
        name = example_api_response['businesses'][0]['name']
        self.assertNotEqual(mock_name, name)

    # Testing API response when restaurant field is None
    @patch('requests.get')
    def test_restaurant_name_none(self, mock_requests_get):
        mock_name = None
        example_api_response = {'businesses': [{'id': '5K82sS0qi4hCnNXzc0mM3A', 'alias': 'revival-minneapolis', 'name': None, 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/JkWblFghKi0DgZNUbvevcQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/revival-minneapolis?adjust_creative=xU677u-VOS4Ysa92q5sRwg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=xU677u-VOS4Ysa92q5sRwg', 'review_count': 1020, 'categories': [{'alias': 'southern', 'title': 'Southern'}, {'alias': 'sandwiches', 'title': 'Sandwiches'}, {'alias': 'bars', 'title': 'Bars'}], 'rating': 4.0, 'coordinates': {'latitude': 44.925208, 'longitude': -93.27771}, 'transactions': ['delivery'], 'price': '$$', 'location': {'address1': '4257 Nicollet Ave', 'address2': '', 'address3': '', 'city': 'Minneapolis', 'zip_code': '55409', 'country': 'US', 'state': 'MN', 'display_address': ['4257 Nicollet Ave', 'Minneapolis, MN 55409']}, 'phone': '+16123454516', 'display_phone': '(612) 345-4516', 'distance': 4599.481096631084}], 'total': 4200, 'region': {'center': {'longitude': -93.2904052734375, 'latitude': 44.96558443188442}}}
        mock_requests_get().json.return_value = example_api_response
        name = example_api_response['businesses'][0]['name']
        self.assertEqual(mock_name, name)

if __name__ == '__main__':
    unittest.main()