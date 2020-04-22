import helper
import pymongo
import bson
from flask import Flask, request, Response
import json
from bson import json_util

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the TODO app!!'

@app.route('/todo/add', methods = ['POST'])
def create_todo():
    req_data = request.get_json()
    name = req_data["name"]
    desc = req_data["desc"]
    priority = req_data["priority"]
    status = req_data["status"]
    data = helper.add_item(name, desc, priority, status)
    if data is None:
        response = Response("{'error': 'Item not added - " + name + "'}", status=400 , mimetype='application/json')
        return response
    
    response = Response(json.loads(data), mimetype='application/json')

    return response
    
@app.route('/todos/all', methods = ['GET'])
def get_all_items():
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    db = client.TODO
    
    data = list(db.todo.find())
    
    return json.dumps(data, default=json_util.default)

@app.route('/todo/update', methods = ['PUT'])
def update_todo():
    req_data = request.get_json()
    name = req_data["name"]
    status = req_data["status"]

    data = helper.update_item(name,status)
    response = Response(json.dumps(data), mimetype='application/json')
    return response

@app.route('/todo/delete', methods = ['DELETE'])
def delete_todo():
    req_data = request.get_json()
    name = req_data["name"]
    data = helper.delete_item(name)
    response = Response(json.dumps(data), mimetype = 'application/json')
    return response
    

if __name__ == '__main__':
    app.run(debug=True)
