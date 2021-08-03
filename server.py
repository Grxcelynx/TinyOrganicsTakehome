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
recipes = recipe_response.json()

allergen_response = requests.get("https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/")
allergen_response.json()


@app.route('/')
def signup():
    """homepage display/ signup page"""

    return render_template('signup.html', allergen=allergen_response.json())


@app.route('/recipes', methods=["POST"])
def tiny_organics():
    """Gathering user data and selection for their recipes"""
    x = request.form.keys()
    # print(f"keys: {x}")
    fname = request.form.get("fname")
    # print(f"FIRST NAME: {fname}")
    lname = request.form.get("lname")
    # print(f"LAST NAME: {lname}")
    email = request.form.get("email")
    # print(f"EMAIL: {email}")
    baby_fname = request.form.get("baby_fname")
    # print(f"BABY FIRST NAME {baby_fname}")
    baby_lname = request.form.get("baby_lname")
    # print(f"BABY LAST NAME: {baby_lname}")
    allergies = request.form.getlist("allergen")
    # print(f"ALLERGIES: {allergies}")



    new_user = crud.create_user(fname,lname,email,baby_fname,baby_lname,allergies)

    #adding recipes that fit user's selections into their result after sumbit.
    users_recipes = []
    for r in recipes:
        matched_allergy = False
        for name in allergies:
            if name in r["allergens"]:
                matched_allergy = True
                break
        if matched_allergy == False:
            users_recipes.append(r)
            
    return render_template('user_recipe.html', new_user=new_user, users_recipes=users_recipes)





if __name__ == '__main__':
    connect_to_db(app)
    # model.db.create_all()
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', debug=True, port=port)