import re
from flask import request, jsonify

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex_pattern = request.args.get('regex')
    data = request.json or {}  # Assuming JSON data is passed in the request body

    for key, value in data.items():
        if regex_pattern and re.search(regex_pattern, str(value)):
            return jsonify({'found': True, 'key': key})  # Return match found with key
    else:
        return jsonify({'found': False, 'message': f"No match found for regex '{regex_pattern}' in data"})