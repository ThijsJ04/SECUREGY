from flask import request, jsonify
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    # Get regex pattern from URL query parameters (if present)
    regex_pattern = request.args.get('regex') or ''
    print(f"Regex pattern: {regex_pattern}")

    # Get data from JSON request body (if present)
    data = request.json if 'data' in request.files else None
    print(f"Data: {data}")

    # Implement regular expression search logic here
    if data is not None and regex_pattern:
        for item in data:
            match = re.search(regex_pattern, item)
            if match:
                return jsonify({'result': 'Match found'})
        return jsonify({'result': 'No match found'})
    else:
        return "Invalid request", 400