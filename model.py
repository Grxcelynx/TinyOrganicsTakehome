from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User(db.model):
    """Data model for a new user"""

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.Text)
    lname = db.Column(db.Text)
    email = db.Column(db.Text, Unique=True)
    baby_fname = db.Column(db.Text)
    baby_lname = db.Column(db.Text)
    allergies = db.Column(db.Text)

class UsersRecipes(db.model):
    """Showing all recipes for each individual customer's needs"""

    __tablename__ = 'users_recipes'

    user_recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    recipe_id = db.Column(db.Integer, db.foreignKey('recipes.recipes_id'))


