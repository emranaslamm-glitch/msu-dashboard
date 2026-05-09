from flask import Flask, jsonify
from flask_cors import CORS
import requests
import time
import os

app = Flask(__name__)
CORS(app)

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwjR6tFIV7fZJfGQII2VElCYac8v0DkdOqSxqmyNNK_MlF0yAWQHGmGSUvnfhqUqX14iGsBmAU1uhX/pub?gid=1773548568&single=true&output=csv"

@app.route('/data')
def get_data():
    response = requests.get(CSV_URL, params={'t': time.time()})
    return jsonify({"csv": response.text})

@app.route('/')
def home():
    with open('dashboard.html') as f:
        return f.read()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
