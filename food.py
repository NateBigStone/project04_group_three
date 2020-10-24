import requests
import re
import time
import os
import logging

logging.basicConfig(level=logging.DEBUG)


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
    # response = request_dishes(dish_input)
    #
    # if response == "error":
    #     return response
    # else:
    dishes_found = convert_response({"q":"chicken","from":0,"to":10,"more":True,"count":120230,"hits":[
        {"recipe":{"uri":"http://www.edamam.com/ontologies/edamam.owl#recipe_b79327d05b8e5b838ad6cfd9576b30b6","label":"Chicken Vesuvio One","image":"https://www.edamam.com/web-img/e42/e42f9119813e890af34c259785ae1cfb.jpg","source":"Serious Eats","url":"http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html","shareAs":"http://www.edamam.com/recipe/chicken-vesuvio-b79327d05b8e5b838ad6cfd9576b30b6/chicken","yield":4.0,"dietLabels":["Low-Carb"],"healthLabels":["Peanut-Free","Tree-Nut-Free"],"cautions":["Sulfites"],"ingredientLines":["1/2 cup olive oil","5 cloves garlic, peeled","2 large russet potatoes, peeled and cut into chunks","1 3-4 pound chicken, cut into 8 pieces (or 3 pound chicken legs)","3/4 cup white wine","3/4 cup chicken stock","3 tablespoons chopped parsley","1 tablespoon dried oregano","Salt and pepper","1 cup frozen peas, thawed"]}},
        {"recipe":{"uri":"http://www.edamam.com/ontologies/edamam.owl#recipe_b79327d05b8e5b838ad6cfd9576b30b6","label":"Chicken Vesuvio Two","image":"https://www.edamam.com/web-img/e42/e42f9119813e890af34c259785ae1cfb.jpg","source":"Serious Eats","url":"http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html","shareAs":"http://www.edamam.com/recipe/chicken-vesuvio-b79327d05b8e5b838ad6cfd9576b30b6/chicken","yield":4.0,"dietLabels":["Low-Carb"],"healthLabels":["Peanut-Free","Tree-Nut-Free"],"cautions":["Sulfites"],"ingredientLines":["1/2 cup olive oil","5 cloves garlic, peeled","2 large russet potatoes, peeled and cut into chunks","1 3-4 pound chicken, cut into 8 pieces (or 3 pound chicken legs)","3/4 cup white wine","3/4 cup chicken stock","3 tablespoons chopped parsley","1 tablespoon dried oregano","Salt and pepper","1 cup frozen peas, thawed"]}},
        {"recipe":{"uri":"http://www.edamam.com/ontologies/edamam.owl#recipe_b79327d05b8e5b838ad6cfd9576b30b6","label":"Chicken Vesuvio Three","image":"https://www.edamam.com/web-img/e42/e42f9119813e890af34c259785ae1cfb.jpg","source":"Serious Eats","url":"http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html","shareAs":"http://www.edamam.com/recipe/chicken-vesuvio-b79327d05b8e5b838ad6cfd9576b30b6/chicken","yield":4.0,"dietLabels":["Low-Carb"],"healthLabels":["Peanut-Free","Tree-Nut-Free"],"cautions":["Sulfites"],"ingredientLines":["1/2 cup olive oil","5 cloves garlic, peeled","2 large russet potatoes, peeled and cut into chunks","1 3-4 pound chicken, cut into 8 pieces (or 3 pound chicken legs)","3/4 cup white wine","3/4 cup chicken stock","3 tablespoons chopped parsley","1 tablespoon dried oregano","Salt and pepper","1 cup frozen peas, thawed"]}}
        ]})
    return dishes_found


def request_dishes(dish_input):
    key = os.environ.get('RECIPE_KEY')
    headers = {'x-rapidapi-host': "edamam-recipe-search.p.rapidapi.com", 'x-rapidapi-key': key}
    url = os.environ.get('RECIPE_URL')
    querystring = {"q": dish_input}

    print(key)
    print(url)
    for i in range(3):
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response)
            if response.status_code != 200:
                print("Unable to connect to API, retrying in 5 seconds.")
                break
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
        return response
    else:
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


def search_restaurant(dishes_found):
    print("\n")
    yelp_dish = input("Please enter name of dish you'd like to search on yelp: ").title()
    
    while yelp_dish not in dishes_found.keys():
        yelp_dish = input("You typed in an incorrect dish name, please try again: ").title()

    return yelp_dish


if __name__ == '__main__':
    main()
