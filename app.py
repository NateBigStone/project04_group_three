from flask import Flask, render_template, request, redirect
import config
from model import Foods
import logging
import json
from database import create_table

app = Flask(__name__)

food_query = Foods()
app.config.from_object(config.Config)
create_table()


@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == 'POST':
        food_query.save_bookmark()
    bookmarks = food_query.get_all_food()
    return render_template('search.html', bookmarks=bookmarks)


@app.route('/item', methods=["GET", "POST"])
def item_endpoint():
    if request.method == 'POST':
        req = request.form
        food_post = req.get("food")
        food_valid = valid_food(food_post)
        if not food_valid:
            return render_template('search.html', error=True, error_text='Invalid input, please try again.')
        else:
            food_query.add_food(food_post)
        return redirect(request.url)
    else:
        try:
            image = food_query.get_image()
            recipe = food_query.get_recipe()
            #json.loads(recipe) turns recipe string back to dictionary recipe_dict
            recipe_dict = json.loads(recipe)
            yelp = food_query.get_yelp()
            if image or recipe or yelp:
                return render_template('search.html', food_response=[image, recipe_dict, yelp])
            else:
                raise Exception
        except Exception as e:
            logging.warning(e)
            return render_template('search.html', error=True, error_text='API error.')


@app.route('/delete', methods=["POST"])
def delete():
    image = request.args.get('image', default=None)
    recipe = request.args.get('recipe', default=None)
    yelp = request.args.get('yelp', default=None)
    food_query.delete_food(yelp, recipe, image)
    return redirect('/')


def valid_food(food_string):
    if food_string.isalpha():
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()
