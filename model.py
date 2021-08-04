from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()

class User(db.Model):
    """Data model for a new user"""

    __tablename__ = 'user_mine'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.Text)
    lname = db.Column(db.Text)
    email = db.Column(db.Text)
    # email = db.Column(db.Text, unique=True) <= for future when wanting to filter emails already used 
    baby_fname = db.Column(db.Text)
    baby_lname = db.Column(db.Text)
    allergies = db.Column(db.Text)



def connect_to_db(flask_app, db_uri='postgresql:///tinyOrganics', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

if __name__ ==  '__main__':
    from server import app
    db_URI = os.getenv('HEROKU_POSTGRESQL_SILVER_URL', 'postgresql:///tinyOrganics')
    if db_URI.startswith("postgres://"):
        db_URI = db_URI.replace("postgres://", "postgresql://", 1)
    print(f"SHOWING DB URL STUFF: {db_URI}")
    connect_to_db(app, db_uri=db_URI)
    

