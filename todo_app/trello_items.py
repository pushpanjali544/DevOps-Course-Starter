import os
import requests
import json
from todo_app.Item import Item
import pymongo
from bson.objectid import ObjectId

# Get environment variables
def Get_trello_APIkey():
    return os.getenv('TRELLOAPIKEY')

def Get_trello_APIToken():
    return os.getenv('TRELLOAPITOKEN')

def Get_trello_APITODOID():
    return os.getenv('TODOID')

def Get_trello_APIDOING():
    return os.getenv('DOING')
    
def Get_items_from_mongodb():
  client=pymongo.MongoClient(os.getenv('MONGODB')) 
  db = client[os.getenv('MONGODBDATABASE')]
  collection = db.test_collection
  todoitemList=[]
  for todoitem in collection.find():
      todoitemList.append(Item(todoitem['_id'],todoitem['name'],todoitem['status']))
  return todoitemList    

 
def Create_iten_from_mongodb(createitem):
    client=pymongo.MongoClient(os.getenv('MONGODB')) 
    db = client[os.getenv('MONGODBDATABASE')]
    collection = db.test_collection
    collection.insert_one({'name': createitem,'status': 'TODO'})

    

    
    
    

def move_item_from_mongodb(id):
    client=pymongo.MongoClient(os.getenv('MONGODB')) 
    db = client[os.getenv('MONGODBDATABASE')]
    collection = db.test_collection
    filter = { '_id':  ObjectId(id) }
    newvalues = { "$set": { 'status': 'DONE' } }
    collection.update_one(filter, new_values)






    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

