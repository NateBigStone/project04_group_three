from flask import Flask, render_template, request, redirect


class Foods:
    def __init__(self):
        self.food = ''

    def add_food(self, food):
        self.food = food

    def get_food(self):
        return self.food


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
        return render_template('index.html', food_response=food_query.get_food())


if __name__ == '__main__':
    app.run()
