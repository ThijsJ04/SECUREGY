import re
from flask import request, jsonify

@app.route('/lookup', methods=['POST'])
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    payload = request.get_json()
    regex = payload.get('regex')
    data = payload.get('data', [])

    if not regex or not data:
        return jsonify({'error': 'Invalid request, provide both regex and data.'}), 400

    # Check if the provided regex is valid
    if not re.match(r'^/^[a-zA-Z]+[\w\.-]*$', regex):
        return jsonify({'error': 'Invalid regex pattern.'}), 400

    # Search for regex in the data
    search_results = [result for result in data if re.search(regex, result)]

    if not search_results:
        return jsonify({'message': 'No match found.'}), 200

    # Return all matching results
    return jsonify([search_result['key'] for search_result in search_results]), 200