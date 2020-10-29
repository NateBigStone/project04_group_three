from flask import Flask, render_template, request, redirect
import config
from model import Foods

app = Flask(__name__)

food_query = Foods()
app.config.from_object(config.Config)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/item', methods=["GET", "POST"])
def item_endpoint():
    if request.method == 'POST':
        req = request.form
        food_post = req.get("food")
        food_query.add_food(food_post)
        return redirect(request.url)
    else:
        return render_template('search.html', food_response=[food_query.get_image(), food_query.get_recipe(),
                                                             food_query.get_yelp()])


if __name__ == '__main__':
    app.run()
