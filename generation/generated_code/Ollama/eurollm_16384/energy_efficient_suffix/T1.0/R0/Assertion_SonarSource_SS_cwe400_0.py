import re
from flask import request, jsonify

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    """
    try:
        # Get regex pattern from request
        pattern = re.compile(re.escape(request.args.get('pattern', '')))

        # Get data from request (as JSON)
        data_json = request.get_json()
        if not data_json:
            return jsonify({'error': 'No data provided'}), 400

        # Search for regex in data
        search_result = any(pattern.fullmatch(data) for data in data_json['data'])

        if search_result:
            return jsonify({'status': 'Match found'}), 200
        else:
            return jsonify({'status': 'No match found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500