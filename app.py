from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Path to the JSON file where the restaurant data will be stored
RESTAURANTS_FILE = 'restaurants.json'


def load_restaurants():
    try:
        with open(RESTAURANTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_restaurants(restaurants):
    with open(RESTAURANTS_FILE, 'w') as file:
        json.dump(restaurants, file, indent=4)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        password = request.form['password']

        meal_items = request.form.getlist('meal_item')
        meal_prices = request.form.getlist('meal_price')

        meals = [{'item': item, 'price': price} for item, price in zip(meal_items, meal_prices)]

        restaurant = {
            'name': name,
            'number': number,
            'password': password,
            'meals': meals
        }

        restaurants = load_restaurants()
        restaurants.append(restaurant)
        save_restaurants(restaurants)

        return redirect(url_for('index'))

    return render_template('register.html')


@app.route('/order', methods=['GET', 'POST'])
def order():
    restaurants = load_restaurants()

    if request.method == 'POST':
        # Handle order form submission (not shown here)
        pass

    return render_template('order.html', restaurants=restaurants)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
