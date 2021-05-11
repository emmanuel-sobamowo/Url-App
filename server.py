from flask import Flask, jsonify, request
from flask_cors import CORS


server = Flask(__name__)
CORS(server)

server.run(debug=True)

@server.route('/') 
def home(): 
    return jsonify({})
