import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.users import userRegister
from resources.item import Item, ListItem
from resources.store import Store, ListStore
from dbfile import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///DataFile.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = "Logan"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ListItem, '/fetch/items')

api.add_resource(Store, '/store/<string:name>')
api.add_resource(ListStore, '/fetch/stores')

api.add_resource(userRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
