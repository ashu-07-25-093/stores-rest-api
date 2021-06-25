import os
from db import db
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql://icgomvabelsknj:c909c6f035da2068e9b5efdb606de3e4bb47ff97da069c7c20848e9772a727b2@ec2-54-158-232-223.compute-1.amazonaws.com:5432/d6p5ul8hbln90m','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Aashu'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')  # '127.0.0.1:5000/item/chair'
api.add_resource(ItemList, '/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister, '/register')     # we register user as by adding resource

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
