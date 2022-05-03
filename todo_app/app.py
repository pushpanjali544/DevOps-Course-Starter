from flask import Flask, render_template, redirect, url_for, request
from flask.globals import session
from todo_app.data.session_items import add_item, get_items
from todo_app.trello_items import  Create_iten_from_mongodb,move_item_from_mongodb, Get_items_from_mongodb
from todo_app.view_model import ViewModel
from pymongo import MongoClient
import os
from flask_login import login_required,LoginManager, UserMixin, login_user, current_user, AnonymousUserMixin
import requests

class User(UserMixin) :
  def __init__(self, user_id):
        self.id = user_id
        if self.id =='pushpanjali544':
           self.role='write_user'
        else:
           self.role='read_user'

class AnonymousUser(AnonymousUserMixin):
        role='write_user'
           
       


def Get_MONGODB():
    return os.getenv('MONGODB')

def Get_MONGODATABASE():
    return os.getenv('DATABASENAME')


def create_app():
    app = Flask(__name__)
    # We specify the full path and remove the import for this config so
    # it loads the env variables when the app is created, rather than
    #when this file is imported
    app.config.from_object('todo_app.flask_config.Config')
    # All the routes and setup code etc
    @app.route('/')
    @login_required
    def index(): 
        items = Get_items_from_mongodb()
        item_view_model = ViewModel(items)
        return render_template("index.html", view_model=item_view_model,role=current_user.role)
        
    @app.route('/', methods=['POST'])
    def add_todo(): 
        if current_user.role=='read_user':
            return 'Forbidden',401
        item = request.form.get('additem')
        Create_iten_from_mongodb(item)
        return redirect('/')

    @app.route('/move', methods=['POST'])
    def Move_InTrello(): 
        if current_user.role=='read_user':
            return 'Forbidden',401
        item = request.form.get('id')
        move_item_from_mongodb(item)
        return redirect('/')

    @app.route('/login/callback')
    def CallbackLogin():
        args = request.args
        code= args.get("code")
        username=''
        url = 'https://github.com/login/oauth/access_token'
        urluser='https://api.github.com/user'
        myobj = {'client_id':os.getenv('Client_ID'), 'client_secret':os.getenv('ClientSecret'),'code':code}

        accesstokenresponse = requests.post(url, data = myobj,headers={'Accept': 'application/json'})
        accesstoken=accesstokenresponse.json()['access_token']
        responseuser = requests.get(urluser,headers={'Authorization': 'token '+accesstoken})
        responseusername=responseuser.json()['login']
        user = User(responseusername)
        login_user(user)
        print(responseuser.text)
        return redirect('/')
        


    login_manager = LoginManager()
    login_manager.anonymous_user=AnonymousUser
    @login_manager.unauthorized_handler
    def unauthenticated():
         return redirect(f'https://github.com/login/oauth/authorize?client_id={os.getenv("Client_ID")}') 
         
    # Github OAuth flow when unauthenticated
    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)
    login_manager.init_app(app)


    return app

