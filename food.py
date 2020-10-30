import requests
import os
import re
import time
import shelve


def main():
    dishes_found = {}
    yelp_dish = ""

    while dishes_found == {}:
        dish_input = get_dish()
        dishes_found = get_dish_info(dish_input)

        if dishes_found == "error":
            break

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
    response = request_dishes(dish_input)

    if response == "error":
        return response
    else:
        dishes_found = convert_response(response)
        return dishes_found


def request_dishes(dish_input):
    cached_response = check_cache(dish_input)
    
    if cached_response != None:
        print("Item found in cache")
        return cached_response.json()
    
    key = os.environ.get('RECIPE_KEY')
    headers = {'x-rapidapi-host': "edamam-recipe-search.p.rapidapi.com", 'x-rapidapi-key': key}
    url = os.environ.get('RECIPE_URL')
    querystring = {"q": dish_input}

    for i in range(3):
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            if response.status_code != 200:
                print("Unable to connect to API, retrying in 5 seconds.")
                time.sleep(5)
                if i == 2:
                    response = "error"
            else:
                break
        except requests.HTTPError:
            print("Service is unavailable or your internet is down. Please try again later.")
            response = "error"
            break
        except Exception:
            print("An error has occurred, please contact our support center.")
            response = "error"
            break
    if response == "error":
        print("We were unable to contact the API, sorry.")
        return response
    else:
        add_cache(dish_input, response)
        return response.json()
    
    
def check_cache(dish_input):
    s = shelve.open("food_cache")

    user_input = input("Would you like to clear cached items?")
    while True:
        if user_input == "Y" or user_input == "y":
            s.close()
            s = shelve.open("food_cache", flag='n')
            break
        elif user_input == "N" or user_input == "n":
            break
        else:
            user_input = input("Sorry I didn't get that, would you like to clear items from your cache?")

    item_found = s.get(dish_input)
    s.close()
    return item_found


def add_cache(dish_input, response):
    s = shelve.open("food_cache")
    s[dish_input] = response


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


def search_restaurant(dishes_found):
    print("\n")
    yelp_dish = input("Please enter name of dish you'd like to search on yelp: ").title()

    while yelp_dish not in dishes_found.keys():
        yelp_dish = input("You typed in an incorrect dish name, please try again: ").title()

    return yelp_dish


if __name__ == '__main__':
    main()
