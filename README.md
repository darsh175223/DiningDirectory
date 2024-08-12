# Dining Directory

Dining Directory is a Flask-based web application that allows restaurants to register and list their meals, and users to browse restaurants and place orders. The application features a user-friendly interface and is designed with an appealing visual style. 

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Installation

### Prerequisites

- Python 3.x
- Flask

### Clone the Repository

```bash
git clone https://github.com/yourusername/dining-directory.git
cd dining-directory
```

### Install Dependencies

Create a virtual environment and install the required dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Running the Application

To start the Flask application, run the following command:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5001/` in your web browser.

## Features

- **Restaurant Registration:** Restaurants can register by providing their name, contact number, and meals.
- **Add Meals:** Restaurants can dynamically add multiple meals with corresponding prices during registration.
- **Meal Ordering:** Users can browse restaurants, view their available meals, and place orders.
- **Responsive Design:** The application features a responsive design with a clean and modern UI.

## Usage

### Registering a Restaurant

1. Go to the Register page (`/register`).
2. Fill in the restaurant's name and contact number.
3. Add a meal by entering the meal name and price, then click the "Add Meal" button to add additional meals.
4. Enter a password for the restaurant's account.
5. Click the "Register" button to save the restaurant and its meals.

### Placing an Order

1. Go to the Order page (`/order`).
2. Select a restaurant from the dropdown list.
3. View the list of meals offered by the restaurant.
4. Check the meals you want to order.
5. Click the "Order Now" button to place the order.

## Project Structure

```plaintext
Dining Directory/
│
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── index.html           # Homepage template
│   ├── order.html           # Order page template
│   └── register.html        # Registration page template
│
├── static/                  # Static files (CSS, JS, images)
│   ├── css/
│   └── images/
│
├── app.py                   # Flask application
├── restaurants.json         # JSON file storing registered restaurants and meals
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```


## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure your changes are well-documented and tested.

