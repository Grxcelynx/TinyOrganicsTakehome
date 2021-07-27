from flask import (Flask, render_template, request, flash, session, redirect, jsonify)

from model import connect_to_db 
import model
import os
import requests 
import json

app = Flask(__name__)
app.secret_key = "dev"

# recipe_response = requests.get("https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/")
# print(recipe_response.json())
# print("##################")
# recipe_dict = json.loads(recipe_response.json)

allergen_response = requests.get("https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/")
allergen_response.json()

# @app.route('/signup', methods=["POST"])
# def signup():
#     data = request.get_json()

@app.route('/')
def homepage():
    """homepage"""
    
    return render_template('homepage.HTML', allergen=allergen_response.json())


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True, port=5000)