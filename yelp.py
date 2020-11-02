import requests
import logging
import os
import shelve


# Makes request to the yelp API using the search_term as a parameter
# returns the response in json format, to be used in the "get_business_name(data)" function
def api_request(search_term):
    cached_response = check_cache(search_term)
    
    if cached_response != None:
        print("Item found in cache.\n")
        return cached_response
    
    api_key = os.getenv('YELP_KEY')
    url = os.getenv('YELP_URL')
    log = logging.getLogger()

    try:
        headers = {'Authorization':'Bearer %s' % api_key}
        params = {'term':'%s' % search_term,'location':'Minneapolis'}
        req = requests.get(url, params=params, headers=headers)
        data = req.json()
        add_cache(search_term, data)
        return get_business_name(data)
    # Researched Try/Except functions for requests, information found at URL below:
    # https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
    except requests.exceptions.Timeout:
        log.warning('Request Timed Out: ' + req)
    except requests.exceptions.TooManyRedirects:
        log.warning('Redirect error- URL may be bad. Check URL, headers, params')
    except requests.exceptions.RequestException as e:
        log.critical('Catastrophic error - exiting program')
        
        
def check_cache(search_term):
    s = shelve.open("yelp_cache")

    # user_input = input("Would you like to clear cached items?")
    # while True:
    #     if user_input == "Y" or user_input == "y":
    #         s.close()
    #         s = shelve.open("yelp_cache", flag='n')
    #         break
    #     elif user_input == "N" or user_input == "n":
    #         break
    #     else:
    #         user_input = input("Sorry I didn't get that, would you like to clear items from your cache?")

    item_found = s.get(search_term)
    s.close()
    return item_found


def add_cache(search_term, data):
    s = shelve.open("yelp_cache")
    s[search_term] = data


# Takes the 'data' from req.json() and returns the 1st business's name from the api response
def get_business_name(data):
    business_name = data['businesses'][0]['name']
    return business_name
