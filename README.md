# Tiny Organics Takehome 

## This takehome assignment was to develop and launch a mini site with specified features such as: 

1. As a new `Customer`, I should be able to access the home page which contains a form which I will enter my information such as:
    1. first name 
    2. last name
    3. email
    4. child's first name
    5. child's last name
    6. any allergies
2. As a new `Customer` , I should be given a list of recipes that do **NOT** contain any ingredients that my child is allergic to.

To make things a bit simpler, TinyOrganics has an API which it makes available via a `GET` request to fetch the list of the BIG-8 allergens and our recipes. 

- To fetch the list of `recipes` , make a `GET` request to `https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/`
- To fetch the list of `allergens`, make a `GET` request to `https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/`

Your project should fetch the list of recipes, store them in the database, and filter out any recipes that contain allergens which the child is allergic to. Remember, we don't wanna harm the little babies.

## Contents
* [Tech Stack](#teach-stack)
* [Features](#features)
* [Future Feature Adjustments](#future)
* [Installation](installation)

## <a name="tech-stack"></a> Technologies      
* Python
* Flask
* Jinja2
* PostgresQL
* SQLAlchemy 
* HTML
* Bootstrap

## <a name="features"></a>Features
By fetching data from the two APIs supplied by Tiny Organics:

### Homepage 
A user can fill out the set fields and select the allergens that apply to their child. 

Created a user class and seeded all user input into the Tiny Organics database. 

With a POST method retrieving user's data and referencing the APIs each time a new user submits a form, this allows for a more accurate comparison vs creating a Json file with the data as there would be more maintenance with checking the API data to assure any changes. 

### Results Page
Here a user will be able to view the recipes that suit their child's needs and display the allergens that do not apply. 

By taking in the user's input and comparing it to the list of allergens, the user is given the result of a new list of recipes that fit their needs. 
## <a name="future"></a> Future Feature Adjustments
* Implement a section for a user to type additional allergies and compare their input to the allergy list
* Make the email key unique so a user will know if an email has been taken 

## <a name="installation"></a>Installation

To run Tiny Organics Takehome:

Clone this repo:
```
https://github.com/Grxcelynx/TinyOrganicsTakehome.git
```

Create and activate a virtual environment inside your Tiny Organics directory:

```
virtual env
source env/bin/activate
```

Install the dependencies:
```
pip install -r requirements.txt
```

Set up the database:

```
dropdb tinyOrganics 
createdb tinyOrganics
python3.6 model.py
```

Run the app:

```
python3.6 server.py
```

You can now navigate to 'localhost:5000/' to access Tiny Organics Takehome.


