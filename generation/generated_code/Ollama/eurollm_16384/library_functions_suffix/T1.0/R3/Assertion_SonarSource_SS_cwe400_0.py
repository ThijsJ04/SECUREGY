from flask import request, jsonify
import re

@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get('regex')
    data = request.args.get('data')

    # Perform the regex search and return a JSON response
    match = re.search(regex, data)
    if match:
        return jsonify({'result': 'Match found'})
    else:
        return jsonify({'result': 'No match found'})