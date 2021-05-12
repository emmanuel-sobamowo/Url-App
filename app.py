from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, g
# from flask_cors import CORS
from hashids import Hashids
import sqlite3


def get_db_connection():
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    return db



app = Flask(__name__)
# CORS(app)

app.config['SECRET_KEY'] = 'this should be a secret random string'

hashids = Hashids(min_length=5, salt=app.config['SECRET_KEY'])
# hashid = hashids.encode(8)
# print(hashid)



@app.route('/', methods=('GET', 'POST'))
def home():
    db = get_db_connection()

    if request.method == 'POST':
        url = request.form['url']

        if not url:
            flash('The URL is needed!')
            return redirect(url_for('home'))

        url_data = db.execute('INSERT INTO urls (original_url) VALUES (?)',
                                (url,))
        db.commit()
        db.close()

        url_id = url_data.lastrowid
        hashid = hashids.encode(url_id)
        short_url = request.host_url + hashid
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')


