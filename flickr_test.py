import unittest
from unittest import TestCase
from unittest.mock import patch, call
import flickr

class TestFlicker(TestCase):

    #checking to see if the user input is a text
    def test_user_input(self):
        self.assertTrue(flickr.get_item().isalpha)


    # checking the photo with numbers which asserts true hence getting the specific photo that you want
    @patch('requests.Response.json')
    def test_image_by_id(self, mock_requests_json):
        mock_id = '1234567890'   # Any number will do.  
        # As long as the JSON contains the data the program needs, it does not need to be a complete response
        example_api_response = {
        "photos":{
            "page":1,
            "pages":4837,
            "perpage":100,
            "total":"483696",
            "photo":[
        {
            "id":mock_id,
            "owner":"80321755@N04",
            "secret":"d224431ee2",
            "server":"7249",
            "farm":8,
            "title":"tacos",
            "ispublic":1,
            "isfriend":0,
            "isfamily":0
        }
            ]
        }
        }   
        mock_requests_json.return_response = [example_api_response] 
         
    
        self.assertTrue('8487666183', mock_id)

    #checking the photo by the wrong id which asserts not equal hence not able to get specific photo
    @patch('requests.Response.json')
    def test_image_by_wrong_id(self, mock_requests_json):
        mock_id = 'abfgikle90'   # Any number will do.  
        # As long as the JSON contains the data the program needs, it does not need to be a complete response
        example_api_response = {
        "photos":{
            "page":1,
            "pages":4837,
            "perpage":100,
            "total":"483696",
            "photo":[
        {
            "id":mock_id,
            "owner":"80321755@N04",
            "secret":"d224431ee2",
            "server":"7249",
            "farm":8,
            "title":"tacos",
            "ispublic":1,
            "isfriend":0,
            "isfamily":0
        }
            ]
        }
        }   
        mock_requests_json.return_response = [example_api_response] 
         
    
        self.assertNotEqual('8487666183', mock_id)


    @patch('requests.Response.json')
    def test_image_by_empty_id(self, mock_requests_json):
        mock_id = ''   # Any number will do.  
        # As long as the JSON contains the data the program needs, it does not need to be a complete response
        example_api_response = {
        "photos":{
            "page":1,
            "pages":4837,
            "perpage":100,
            "total":"483696",
            "photo":[
        {
            "id":mock_id,
            "owner":"80321755@N04",
            "secret":"d224431ee2",
            "server":"7249",
            "farm":8,
            "title":"tacos",
            "ispublic":1,
            "isfriend":0,
            "isfamily":0
        }
            ]
        }
        }   
        mock_requests_json.return_response = [example_api_response] 
         
    
        self.assertIsNot('8487666183', mock_id)
