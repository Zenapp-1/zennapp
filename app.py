"""Simple Flask API to serve modules.json for development/testing.
Run: pip install flask && python app.py
"""
from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='.')


@app.route('/api/modules')
def modules_api():
    path = os.path.join(os.path.dirname(__file__), 'modules.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)


@app.route('/')
def index():
    return send_from_directory('.', 'trade-with-suli.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
