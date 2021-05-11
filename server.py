from flask import Flask, jsonify, request
from flask_cors import CORS


CORS(server)

server = Flask(__name__)

server.run(debug=True)

@server.route('/') 
def home(): 
    return jsonify('Hello from Flask!')