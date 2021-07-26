from flask import (Flask, render_template, request, flash, session, redirect, jsonify)

from model import connect_to_db 
import model
import requests 


app = Flask(__name__)
app.secret_key = "dev"

recipe_response = requests.get("https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/")
print(recipe_response.json())
print("##################")

allergen_response = requests.get("https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/")
print(allergen_response.json())





if __name__ == '__main__':
    connect_to_db(app)
    app.run()