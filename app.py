from flask import Flask, jsonify, request
from flask_cors import CORS
from hashids import Hashids

app = Flask(__name__)
CORS(app)

app.run(debug=True)

@app.route('/') 
def home(): 
    return jsonify({})

