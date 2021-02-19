from flask import Flask, render_template, redirect, url_for, request
from flask.globals import session
from todo_app.data.session_items import add_item, get_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index(): 
    items = get_items()
    return render_template("index.html", items=items)
    
@app.route('/', methods=['POST'])
def add_todo(): 
    item = request.form.get('additem')
    add_item(item)
    return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)

