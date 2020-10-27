import requests
import logging
import os


# Makes request to the yelp API using the search_term as a parameter
# returns the response in json format, to be used in the "get_business_name(data)" function
def api_request(search_term):
    api_key = os.getenv('YELP_KEY')
    url = os.getenv('YELP_URL')
    log = logging.getLogger()

    try:
        headers = {'Authorization':'Bearer %s' % api_key}
        params = {'term':'%s' % search_term,'location':'Minneapolis'}
        req = requests.get(url, params=params, headers=headers)
        data = req.json()
        return get_business_name(data)
    # Researched Try/Except functions for requests, information found at URL below:
    # https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
    except requests.exceptions.Timeout:
        log.warning('Request Timed Out: ' + req)
    except requests.exceptions.TooManyRedirects:
        log.warning('Redirect error- URL may be bad. Check URL, headers, params')
    except requests.exceptions.RequestException as e:
        log.critical('Catastrophic error - exiting program')


# Takes the 'data' from req.json() and returns the 1st business's name from the api response
def get_business_name(data):
    business_name = data['businesses'][0]['name']
    return business_name
