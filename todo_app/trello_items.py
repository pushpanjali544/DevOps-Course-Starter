import os
import requests
import json

# Get environment variables
TRELLOAPIKEY = os.getenv('TRELLOAPIKEY')
TRELLOAPITOKEN = os.environ.get('TRELLOAPITOKEN')
TODOID='6048d81adf46ed3c0e396169'
DOING='6048d81adf46ed3c0e39616a'
def Get_items_from_trello():
    print(TRELLOAPIKEY)
    print(TRELLOAPITOKEN)


    #url = 'https://api.trello.com/1/members/me/boards'

    url = "https://api.trello.com/1/boards/6048d81adf46ed3c0e396168/cards"

    query = {
    'key': TRELLOAPIKEY,
    'token': TRELLOAPITOKEN
    }

    response = requests.request(
    "GET",
    url,
    params=query
    )

    
    response=response.json()
    for card in response:
        if card['idList']==TODOID:
            card['status']='TODO'
        elif card['idList']== DOING:
            card['status']='DOING'



    return response

def create_card(name_of_card):
    url = "https://api.trello.com/1/cards"
    query = {
    'key': TRELLOAPIKEY,
    'token':TRELLOAPITOKEN,
    'idList': TODOID,
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
    'key': TRELLOAPIKEY,
    'token': TRELLOAPITOKEN,
    'idList':DOING
    }

    response = requests.request(
    "PUT",
    url,
    headers=headers,
    params=query
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

