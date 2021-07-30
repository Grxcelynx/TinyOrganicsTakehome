from flask_sqlalchemy import SQLAlchemy

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

if __name__ ==  '__main__':
    from server import app

    connect_to_db(app)
    

