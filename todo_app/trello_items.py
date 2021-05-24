import os
import requests
import json
from todo_app.Item import Item

# Get environment variables
def Get_trello_APIkey():
    return os.getenv('TRELLOAPIKEY')

def Get_trello_APIToken():
    return os.getenv('TRELLOAPITOKEN')

def Get_trello_APITODOID():
    return os.getenv('TODOID')

def Get_trello_APIDOING():
    return os.getenv('DOING')

def Get_trello_APIDONE():
    return os.getenv('DONE')

def Get_items_from_trello():
   
    #url = 'https://api.trello.com/1/members/me/boards'

    url = f"https://api.trello.com/1/boards/{os.getenv('BOARDID')}/cards"

    query = {
    'key': Get_trello_APIkey(),
    'token': Get_trello_APIToken()
    }

    response = requests.request(
    "GET",
    url,
    params=query
    )

    
    response=response.json()
    for card in response:
        if card['idList']==Get_trello_APITODOID():
            card['status']='TODO'
        elif card['idList']== Get_trello_APIDOING():
            card['status']='DOING'


    idList=[]
    for card in response:
        idList.append(Item(card['id'],card['name'],card['status'],card['idList']))
        
    return idList

def create_card(name_of_card):
    url = "https://api.trello.com/1/cards"
    query = {
    'key': Get_trello_APIkey(),
    'token':Get_trello_APIToken(),
    'idList': Get_trello_APITODOID(),
    'name': name_of_card
    }
    response = requests.request(
    "POST",
    url,
    params=query
    )

def move_card(id):
    url = f"https://api.trello.com/1/cards/{id}"

    headers = {
    "Accept": "application/json"
    }

    query = {
    'key': Get_trello_APIkey(),
    'token': Get_trello_APIToken(),
    'idList':Get_trello_APIDOING()
    }

    response = requests.request(
    "PUT",
    url,
    headers=headers,
    params=query
    )

def create_trello_board():
    url = "https://api.trello.com/1/boards/"
    query = {
    'key': Get_trello_APIkey(),
    'token':Get_trello_APIToken(),
    'name': 'SeleniumTestBoard'
    }
    response = requests.request(
    "POST",
    url,
    params=query
    )

def delete_trello_board(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}"
    query = {
    'key': Get_trello_APIkey(),
    'token':Get_trello_APIToken()
    }
    response = requests.request(
    "DELETE",
    url,
    params=query
    )


    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

