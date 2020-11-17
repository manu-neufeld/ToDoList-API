"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Task
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_all_user():
    try:
        all_users = User.get_user()
        return jsonify(all_users), 200
    except:
        return "Do not found users", 400

@app.route('/user/<username>', methods=['GET'])
def read_user(username):
    try:
        user=User.get_user(username)
        return jsonify(user), 200
    except:
        return "user not found", 400

@app.route('/todos/user/<username>', methods=['POST'])
def create_user(username):
    
    new_user= User(user_name= username)
    new_user.add_user()

    return jsonify(new_user.serialize()), 200

@app.route('/todos/user/<username>', methods=['DELETE'])
def delete_user(username):
    User.delete_user(username)

@app.route('/todos/user/<username>/task', methods=['POST'])
def create_tasks(username):
    body=request.get_json()
  
    new_task = Task(user_to_do= username ,label=body["label"],done=body["done"])
    new_task.add_task()

    return jsonify(new_task.serialize())

@app.route('/todos/user/<username>/task', methods=['GET'])
def read_task(username):
    try:
        tasks=Task.read_all_tasks(username)
        return tasks, 200
    except:
        return "there are not task", 400

@app.route('/todos/user/<username>/task/<int:id>', methods=['PUT'])
def update(id):
    try:
        body=request.get_json()
        Task.update_task(id, body['label'], body['done'])
        return "task updated", 200
    except:
        return "task not found", 400



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)