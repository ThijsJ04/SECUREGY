import re
from flask import request, jsonify

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    data = request.get_json()  # Assuming the request comes in JSON format
    regex = request.json['pattern']

    if regex:  # Check if the pattern exists
        for item in data:
            if re.search(regex, str(item)):
                return jsonify({'message': 'Match found'})
    else:
        return jsonify({'message': 'No match found'})