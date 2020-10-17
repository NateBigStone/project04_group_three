from flask import Flask, render_template, request, redirect
from model import Foods

app = Flask(__name__)

food_query = Foods()


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
        return render_template('index.html', food_response=food_query.get_recipe())


if __name__ == '__main__':
    app.run()
