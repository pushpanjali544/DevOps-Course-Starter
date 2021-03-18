from flask import Flask, render_template, redirect, url_for, request
from flask.globals import session
from todo_app.data.session_items import add_item, get_items
from todo_app.flask_config import Config
from todo_app.trello_items import Get_items_from_trello, create_card,move_card


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index(): 
    items = Get_items_from_trello()
    return render_template("index.html", items=items)
    
@app.route('/', methods=['POST'])
def add_todo(): 
    item = request.form.get('additem')
    create_card(item)
    return redirect('/')

@app.route('/move', methods=['POST'])
def Move_InTrello(): 
    item = request.form.get('id')
    move_card(item)
    return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)

