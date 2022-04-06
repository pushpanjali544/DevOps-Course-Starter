from flask import Flask, render_template, redirect, url_for, request
from flask.globals import session
from todo_app.data.session_items import add_item, get_items
from todo_app.trello_items import  Create_iten_from_mongodb,move_item_from_mongodb, Get_items_from_mongodb
from todo_app.view_model import ViewModel
from pymongo import MongoClient
import os

def Get_MONGODB():
    return os.getenv('MONGODB')

def Get_MONGODATABASE():
    return os.getenv('DATABASENAME')


def create_app():
    client = MongoClient(Get_MONGODB())
    db=client[Get_MONGODATABASE()]
    collection = db.test_collection
    app = Flask(__name__)
    # We specify the full path and remove the import for this config so
    # it loads the env variables when the app is created, rather than
    #when this file is imported
    app.config.from_object('todo_app.flask_config.Config')
    # All the routes and setup code etc
    db = client.test_database
    @app.route('/')
    def index(): 
        items = Get_items_from_mongodb()
        item_view_model = ViewModel(items)
        return render_template("index.html", view_model=item_view_model)
        
    @app.route('/', methods=['POST'])
    def add_todo(): 
        item = request.form.get('additem')
        Create_iten_from_mongodb(item)
        return redirect('/')

    @app.route('/move', methods=['POST'])
    def Move_InTrello(): 
        item = request.form.get('id')
        move_item_from_mongodb(item)
        return redirect('/')

    return app
