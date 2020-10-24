import requests
import json
import logging

api_key='<CHECK SLACK CHAT FOR THIS>'
url = 'https://api.yelp.com/v3/businesses/search'


# Makes request to the yelp API using the search_term as a parameter
# returns the response in json format, to be used in the "get_business_name(data)" function
def api_request(search_term):
    try:
        headers = {'Authorization':'Bearer %s' % api_key}
        params = {'term':'%s' % search_term,'location':'Minneapolis'}
        req = requests.get(url, params=params, headers=headers)
        data = req.json()
        return data
    # Researched Try/Except functions for requests, information found at URL below:
    # https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
    except requests.exceptions.Timeout:
        log('Request Timed Out: ' + req)
    except requests.exceptions.TooManyRedirects:
        log('Redirect error- URL may be bad. Check URL, headers, params')
    except requests.exceptions.RequestException as e:
        log('Catastrophic error - exiting program')
        raise SystemExit(e)


# Takes the 'data' from req.json() and returns the 1st business's name from the api response
def get_business_name(data):
    business_name = data['businesses'][0]['name']
    return business_name