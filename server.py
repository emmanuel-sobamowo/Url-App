from flask import Flask, jsonify, request
from flask_cors import CORS
from hashids import Hashids

server = Flask(__name__)
CORS(server)

server.run(debug=True)

@server.route('/') 
def home(): 
    return jsonify({})

hashids = Hashids(salt= 'this is my salt')
id = hashids.encode(1, 2, 3)
numbers = hashids.decode(id)

print(id)
print(numbers)