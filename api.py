from flask import Flask, jsonify, request
from printing import print_label

app = Flask(__name__)

@app.route('/print', methods=['POST'])
def print():
    data = request.get_json()

    if 'text' not in data:
        return "Missing 'text' field", 400

    print_label(data['text'])

    return "OK", 200

