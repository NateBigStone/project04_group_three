from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/item', methods=["GET", "POST"])
def item_endpoint():
    if request.method == 'POST':
        req = request.form
        food = req.get("food")
        print(food)
        return redirect(request.url)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
