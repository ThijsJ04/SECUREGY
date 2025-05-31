import re
from flask import request, jsonify

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex')  # Get regex from query string
    data = request.json if 'data' in request.args else request.args.get('data', default='{}')  # Get data from JSON or query string

    if isinstance(data, dict):
        data = json.dumps(data)

    match = re.search(regex, data)
    if match:
        return jsonify({'result': 'Match found'})
    else:
        return jsonify({'result': 'No match found'})