"""crud functions"""
from model import db, User, connect_to_db

def create_user(fname, lname, email, baby_fname, baby_lname, allergies):
    """Create new user"""

    new_user = User(fname=fname, lname=lname, email=email, baby_fname=baby_fname, baby_lname=baby_lname, allergies=allergies)

    db.session.add(new_user)
    db.session.commit()

    return new_user

def get_all_users():
    """Return all users."""

    return User.query.all()
















# !!! for filtering out which emails are used in future. !!!
# def user_emails():
#     """Return all emails."""

#     email_list = []

#     for user in get_all_users():
#         email_list.append(user.email)

#     return email_list

# def get_user_by_email(email):
#     """Returns a user with email."""

#     return User.query.filter(User.email == email).first()

# def get_user_by_email(email):
#     """Return a user by email."""

    # return User.query.filter(User.email == email).first()