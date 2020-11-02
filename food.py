import requests
import os
import re
import time
import shelve #Used for caching API responses.
import logging


def main():
    dishes_found = {}
    yelp_dish = ""
    
    
    #Prompts user for input and prints recipe name/ingredients as long as no error is returned.
    while dishes_found == {}:
        dish_input = get_dish()
        dishes_found = get_dish_info(dish_input)
        
        #Returns an empty string if an error has occured.
        if dishes_found == "error":
            break
        
        #Checks response for 0 hits found
        display_result(dishes_found)
        if dishes_found != {}:
            yelp_dish = search_restaurant(dishes_found)
    return yelp_dish


def get_dish():
    while True:
        dish_input = input('Enter dish name: ').strip().lower()

        if not dish_input.replace(' ', '').isalpha():
            print("Input was either empty or contained an invalid character, please try again.")
            continue
        else:
            dish_input = re.sub(' +', ' ', dish_input)
            break
    return dish_input


def get_dish_info(dish_input):
    #Calls api function with user input as param.
    response = request_dishes(dish_input)
    
    #If error has occured, return "error" instead of converting/displaying.
    if response == "error":
        return response
    else:
        dishes_found = convert_response(response)
        return dishes_found


def request_dishes(dish_input):
    #Calls method to check if user input is in cache, returned response if found.
    cached_response = check_cache(dish_input)
    
    #If not found in shelve, cached_response is set to "None".
    if cached_response != None:
        print("Item found in cache")
        return cached_response.json()
    
    key = os.environ.get('RECIPE_KEY')
    headers = {'x-rapidapi-host': "edamam-recipe-search.p.rapidapi.com", 'x-rapidapi-key': key}
    url = os.environ.get('RECIPE_URL')
    querystring = {"q": dish_input}
    
    #Set max try to contact API with request to 3 times, as long as an error hasn't occured before.
    for i in range(3):
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            if response.status_code != 200:
                print("Unable to connect to API, retrying in 5 seconds.")
                #Rather than spam the API with requests, we delay the next attempt by a few seconds to save on calls/data usage.
                time.sleep(5)
                if i == 2:
                    response = "error"
            else:
                break
        #Logging a few specific request exceptions for support/debugging purposes.
        except requests.HTTPError:
            logging.debug(f'[Error Occured] HTTP - Requests')
            response = "error"
            break
        except requests.ConnectionError:
            logging.debug(f'[Error Occured] Connection - Requests')
            response = "error"
            break
        except requests.Timeout:
            logging.debug(f'[Error Occured] Timeout - Requests')
            response = "error"
            break
        except requests.TooManyRedirects:
            logging.debug(f'[Error Occured] TooManyRedirects - Requests')
            response = "error"
            break
        except Exception:
            logging.debug(f'[Error Occured] Generic/Unknown Error - Requests')
            response = "error"
            break
    if response == "error":
        print("We were unable to contact the API, sorry.")
        return response
    else:
        #Calls method to add the most recent response to the cache.
        add_cache(dish_input, response)
        return response.json()
    
    
def check_cache(dish_input):
    #Creates/Opens shelve to try and find response based on dish name.
    s = shelve.open("food_cache")

    item_found = s.get(dish_input)
    s.close()
    return item_found


def add_cache(dish_input, response):
    s = shelve.open("food_cache")
    s[dish_input] = response

    
#Grab specific elements from json object and store results in a dictionary.
def convert_response(response):
    recipe_name = []
    recipe_ingredients = []

    for items in response['hits']:
        recipe_name.append(items['recipe']['label'])
        recipe_ingredients.append(items['recipe']['ingredientLines'])

    result_dict = {recipe_name[i]: recipe_ingredients[i] for i in range(len(recipe_name))}

    return result_dict


#Prints each Key/Value pair within the dictionary.
def display_result(dishes_found):
    print("\n-------results found-------\n")
    for key, value in dishes_found.items():
        print(f"Dish Name: {key} \nDish Ingredients: {value} \n\n")

        
#Prompts user to select a recipe name from the dictionary based on key.
def search_restaurant(dishes_found):
    print("\n")
    yelp_dish = input("Please enter name of dish you'd like to search on yelp: ").title()

    while yelp_dish not in dishes_found.keys():
        yelp_dish = input("You typed in an incorrect dish name, please try again: ").title()

    return yelp_dish


if __name__ == '__main__':
    main()
