import os

# import crud
import model
import server

os.system('dropdb tinyorganics')
os.system('createdb tinyorganics')

model.connect_to_db(server.app)
model.db.create_all()