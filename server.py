from flask import Flask

server = Flask(__name__)

server.run(debug=True)

@server.route('/') 
def home(): 
    return 'Hello from Flask!' 