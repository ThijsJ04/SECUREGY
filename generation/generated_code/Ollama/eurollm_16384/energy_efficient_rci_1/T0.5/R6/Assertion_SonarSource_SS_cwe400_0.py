import re
from flask import request, jsonify

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex')
    data = request.args.get('data')

    if regex and data:
        match = re.search(regex, data)
        if match:
            return jsonify({'result': 'Match found'})
        else:
            return jsonify({'result': 'No match found'})
    else:
        return "Error: Invalid input parameters", 400