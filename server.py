from flask import Flask, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwjR6tFIV7fZJfGQII2VElCYac8v0DkdOqSxqmyNNK_MlF0yAWQHGmGSUvnfhqUqX14iGsBmAU1uhX/pub?gid=1773548568&single=true&output=csv"

@app.route('/data')
def get_data():
    try:
        response = requests.get(CSV_URL, params={'t': str(time.time())})
        return jsonify({"csv": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    try:
        with open('/Users/mac/MSU_Dashboard/dashboard.html') as f:
            return f.read()
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(port=5000)
