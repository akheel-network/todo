import pymongo
import bson
from pymongo import MongoClient




def add_item(name, desc, priority, status):
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    db = client.TODO
    db.todo.insert_many([{ "name": name, "desc": desc, "priority": priority, "status": status}])
    return 'Entry created successfully'
    
def update_item(name, status):
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    db = client.TODO
    db.todo.update({'name': name}, {'$set':{'status':status}})
    return {name : status}

def delete_item(name):
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    db = client.TODO
    db.todo.remove({'name': name})
    return {name:"Deleted successfully"}
    
    
