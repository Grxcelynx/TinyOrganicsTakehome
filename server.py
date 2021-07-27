#user email already used - check email value and return msg saying already use 
#fetch recipe list and compare to user input of allergens 
#save recipes that go with user's specifications into db
#attempt to convert to react - ATTEMPT 

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)

from model import connect_to_db 
import model
import os
import requests 
import json
import crud

app = Flask(__name__)
app.secret_key = "dev"

recipe_response = requests.get("https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/")
recipe_response.json()
# print("##################")
# recipe_dict = json.loads(recipe_response.json)

allergen_response = requests.get("https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/")
allergen_response.json()

@app.route('/')
def homepage():
    return render_template('homepage.HTML')

@app.route('/signup')
def signup():
    """homepage display/ signup page"""

    
    return render_template('signup.HTML', allergen=allergen_response.json())

@app.route('/recipes', methods=["POST"])
def recipes():
    x = request.form.keys()
    print(f"keys: {x}")
    fname = request.form.get("fname")
    print(f"FIRST NAME: {fname}")
    lname = request.form.get("lname")
    print(f"LAST NAME: {lname}")
    email = request.form.get("email")
    print(f"EMAIL: {email}")
    baby_fname = request.form.get("baby_fname")
    print(f"BABY FIRST NAME {baby_fname}")
    baby_lname = request.form.get("baby_lname")
    print(f"BABY LAST NAME: {baby_lname}")
    allergies = request.form.getlist("allergen")
    print(f"ALLERGIES: {allergies}")

    # if email in crud.user_emails():
    #     return "email used"

    new_user = crud.create_user(fname,lname,email,baby_fname,baby_lname,allergies)


    return render_template('user_recipe.HTML', new_user=new_user, recipes=recipe_response.json())






if __name__ == '__main__':
    connect_to_db(app)
    model.db.create_all()
    app.run(host='0.0.0.0', debug=True, port=5000)