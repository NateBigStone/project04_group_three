import requests
import os
import re
import time
import ast

def main():
    dishes_found = {}

    while dishes_found == {}:
        dish_input = get_dish()
        dishes_found = get_dish_info(dish_input)
        display_result(dishes_found)
        if dishes_found != {}:
            yelp_dish = search_restraunt(dishes_found)

    return yelp_dish

def get_dish():
    while True:
        dish_input = input('Enter dish name: ').strip().lower()

        if not dish_input.replace(' ','').isalpha():
            print("Input was either empty or contained an invalid character, please try again.")
            continue
        else:
            dish_input = re.sub(' +', ' ', dish_input)
            break
    return dish_input

def get_dish_info(dish_input):
    response = request_dishes(dish_input)
    dishes_found = convert_response(response)
    return dishes_found

def request_dishes(dish_input):
    string = os.environ.get('headers')
    headers = ast.literal_eval(string)
    url = "https://rapidapi.p.rapidapi.com/search"
    querystring = {"q":dish_input}

    while True:
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code != 200:
            print("Unable to connect to API, retrying in 15 seconds.")
            time.sleep(15)
        else:
            break

    return response.json()

def convert_response(response):
    recipe_name = []
    recipe_ingredients = []

    for items in response['hits']:
        recipe_name.append(items['recipe']['label'])
        recipe_ingredients.append(items['recipe']['ingredientLines'])

    result_dict = {recipe_name[i]: recipe_ingredients[i] for i in range(len(recipe_name))}
    
    return result_dict

def display_result(dishes_found):
    print("\n-------results found-------\n")
    for key, value in dishes_found.items():
        print(f"Dish Name: {key} \nDish Ingredients: {value} \n\n")

def search_restraunt(dishes_found):
    print("\n")
    yelp_dish = input("Please enter name of dish you'd like to search on yelp: ").title()
    
    while yelp_dish not in dishes_found.keys():
        yelp_dish = input("You typed in an incorrect dish name, please try again: ").title()

    return yelp_dish