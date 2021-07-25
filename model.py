from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Data model for a new user"""

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.Text)
    lname = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    baby_fname = db.Column(db.Text)
    baby_lname = db.Column(db.Text)
    allergies = db.Column(db.Text)

class Allergies(db.Model):
    """Allergens from API"""

    __tablename__ = 'allergies'

    allergy_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    a_created_at = db.Column(db.Text)
    name = db.Column(db.Text, unique=True)

class Recipes(db.Model):
    """Recipes from API"""

    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    r_created_at = db.Column(db.Text)
    allergens_included = db.Column(db.Text)
    name = db.Column(db.Text, unique=True)


class UsersRecipes(db.Model):
    """Showing all recipes for each individual customer's needs"""

    __tablename__ = 'users_recipes'

    user_recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipes_id'))
    allergy_id = db.Column(db.Integer, db.ForeignKey('allergies.allergy_id'))

    user = db.relationship('User', backref='users_recipes')
    recipe = db.relationship('Recipes', backref='recipes')
    allergy = db.relationship('Allergies', backref='allergies')









def connect_to_db(flask_app, db_uri='postgresql:///tinyOrganics', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ ==  '__main__':
    from server import app

    connect_to_db(app)
    

